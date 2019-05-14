import click
from jenkinsapi.jenkins import Jenkins


@click.command()
@click.argument('jenkins_url', envvar='JENKINS_URL')
@click.argument('user_name', envvar='API_USER')
@click.argument('api_token', envvar='API_TOKEN')
@click.option('--find', help='Find Jenkins Job contain keyword')
@click.option('--build', help='Build Jenkins Job')
def dowork(user_name, api_token, find, build):
    if find:
        get_jenkin_job_contain_keyword(user_name, api_token, find)
    if build:
        build_jenkin_job(user_name, api_token, build)

def get_jenkin_job_contain_keyword(user_name, api_token, find):
    server = Jenkins(jenkins_url, user_name, api_token)
    for job_name, job_description in server.get_jobs():
        if find in job_name:
            click.echo("- %s" % job_name)
    
def build_jenkin_job(user_name, api_token, build):
    server = Jenkins(jenkins_url, user_name, api_token)
    if server.has_job(build):
        server.build_job(build)
        click.echo('Jenkins Job %s build' %build)
    else:
        click.echo("Job doesn't exist")


if __name__ == '__main__':
    dowork()