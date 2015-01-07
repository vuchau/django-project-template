from fabric.api import sudo, task


@task
def installchef():
    """
    Install all the dependencies to run a Chef cookbook
    """
    # Install dependencies
    sudo('apt-get update', pty=True)
    sudo(
        'apt-get install -y git-core rubygems1.9.1 ruby1.9.1 \
build-essential ruby1.9.1-dev',
        pty=True
    )
    # Screw ruby docs.
    sudo("echo 'gem: --no-ri --no-rdoc' > /root/.gemrc")
    sudo("echo 'gem: --no-ri --no-rdoc' > /home/ubuntu/.gemrc")
    # Install Chef
    sudo('gem install --no-ri --no-rdoc chef', pty=True)
