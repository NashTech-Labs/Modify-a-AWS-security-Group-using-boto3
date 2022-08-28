# MuZakkir Saifi
# import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError
import json

REGION = input("Please enter the REGION: ")

# this is the configration for the logger_for

logger_for = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

client_for_grp = boto3.client("ec2", region_name=REGION)


def rule_modification(grp_id, grp_rule_id):
    
    try:
        res = client_for_grp.modify_security_group_rules(
            GroupId=grp_id,
            SecurityGroupRules=[
                {
                    'SecurityGroupRuleId': grp_rule_id,
                    'SecurityGroupRule': {
                        'IpProtocol': 'tcp',
                        'FromPort': 8080,
                        'ToPort': 8080,
                        'CidrIpv4': '0.0.0.0/0',
                        'Description': DESCRIPTION
                    }
                },
            ])

    except ClientError:
        logger_for.exception('This Could not modify security group rule.')
        raise
    else:
        return res


if __name__ == '__main__':
    GRP_ID = input("Please enter the Security group ID: ")
    GRP_RULE_ID = input("Please enter the Security group Rule ID: ")
    DESCRIPTION = input("Enter the description for modification: ")
    logger_for.info(f'Please wait, We are modifing your security group rule...')
    result = rule_modification(GRP_ID, GRP_RULE_ID)
    logger_for.info(
        f'Wow!! your Security group rule has been modified: \n{json.dumps(result, indent=4)}')