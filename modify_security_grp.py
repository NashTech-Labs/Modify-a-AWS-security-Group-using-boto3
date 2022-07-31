# import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError
import json

AWS_REGION = input("Please enter the AWS_REGION")

# this is the configration for the logger

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

vpc_client = boto3.client("ec2", region_name=AWS_REGION)


def rule_modification(security_group_id, security_group_rule_id):
    
    try:
        response = vpc_client.modify_security_group_rules(
            GroupId=security_group_id,
            SecurityGroupRules=[
                {
                    'SecurityGroupRuleId': security_group_rule_id,
                    'SecurityGroupRule': {
                        'IpProtocol': 'tcp',
                        'FromPort': 8080,
                        'ToPort': 8080,
                        'CidrIpv4': '0.0.0.0/0',
                        'Description': 'Tech-hub template '
                    }
                },
            ])

    except ClientError:
        logger.exception('This Could not modify security group rule.')
        raise
    else:
        return response


if __name__ == '__main__':
    SECURITY_GROUP_ID = input("Please enter the Security group ID")
    SECURITY_GROUP_RULE_ID = input("Please enter the Security group Rule ID")
    # SECURITY_GROUP_ID = 'sg-022ed25b68ad24c18'
    # SECURITY_GROUP_RULE_ID = 'sgr-02204706ef3300225'
    logger.info(f'Please wait, We are modifing your security group rule...')
    rule = rule_modification(SECURITY_GROUP_ID, SECURITY_GROUP_RULE_ID)
    logger.info(
        f'Wow!! your Security group rule has been modified: \n{json.dumps(rule, indent=4)}')