from atlassian import Jira

API_KEY= "ATATT3xFfGF0C9Sam1yRYHQqP07wBHf6v3qRe2KFWDaQRr6EWfVPLLsoT47JdviMxRcFeBRPNN6j2usIPhyf6_t_qd04-EcUXdeD37I1rTVqIfzt1TNXhyPwN8fDwoxHvBgtOgDonsj3cr1172xjpEy8vyE1JWm6wAOoJVSLFymz4cD2CXpaNj0=ED60C144"
JIRA_URL= "https://ashleyhamiltonnyc.atlassian.net/"
PROJECT_NAME = "SCRUM"

def access_jira_function():
    connection = Jira(
    url=JIRA_URL,
    username='ashleyhamiltonnyc@gmail.com',
    password=API_KEY,cloud= True)
    
    response = connection.jql(f"project = {PROJECT_NAME}")
    for issue in response["issues"]:
        
        # print(issue.keys())
        # breakpoint()
        summary =issue["fields"]["summary"]
        description = issue["fields"]["description"]
        print()
        print("issue#",issue["id"])
        print(summary)
        print(description)

        print(connection.json())

# this should be in every file 
if __name__ == "__main__":
    access_jira_function()

# https://ashleyhamiltonnyc.atlassian.net/

# jira api key 
# ATATT3xFfGF0C9Sam1yRYHQqP07wBHf6v3qRe2KFWDaQRr6EWfVPLLsoT47JdviMxRcFeBRPNN6j2usIPhyf6_t_qd04-EcUXdeD37I1rTVqIfzt1TNXhyPwN8fDwoxHvBgtOgDonsj3cr1172xjpEy8vyE1JWm6wAOoJVSLFymz4cD2CXpaNj0=ED60C144

