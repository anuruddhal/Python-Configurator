#!/usr/bin/env python
from ConfigParserUtil import ConfigParserUtil
import os
import Constants
from distutils import dir_util
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'Templates')),
    trim_blocks=False)


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

def create_output_xml(template_path,output_path,context):
    with open(output_path, 'w') as f:
        content = render_template(template_path, context)
        f.write(content)

def create_template():
    members={"mgt.as.wso2.com": 4100,"as.wso2.com": 4300}
    f = ConfigParserUtil()
    f.read("./configs.ini")
    d = f.as_dict()

    # context={"clustering": '"true"',
    #          "members": members,
    #          "localMemberHost": "127.0.1.1",
    #          "localMemberPort": 4100,
    #          "subDomain": "mgt",
    #          "stratos_instance_data_worker_host_name": "as.wso2.com",
    #          "stratos_instance_data_mgt_host_name": "mgt.as.wso2.com",
    #          "portOffset":1,
    #          "http_proxy_port":80,
    #          "https_proxy_port":443
    #
    #         }
    members= d["DEFAULTS"]["members"]
    #print d["DEFAULTS"]
    d["DEFAULTS"]["members"]=members
    context=d["DEFAULTS"]
    create_output_xml(Constants.AXIS2_TEMPLATE_PATH,Constants.AXIS2_OUTPUT_PATH,context)
    #create_output_xml(Constants.CARBON_TEMPLATE_PATH,Constants.CARBON_OUTPUT_PATH,context)
    # create_output_xml(Constants.CATALINA_SERVER_TEMPLATE_PATH,Constants.CATALINA_SERVER_OUTPUT_PATH,context)
    # dir_util.copy_tree("./Output", "/Users/anuruddha/Downloads/wso2as-5.2.1/repository/conf")

def main():
    create_template()




if __name__ == "__main__":
    main()