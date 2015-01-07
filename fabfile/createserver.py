import boto
import time
from fabric.api import env, task


@task
def create_server(
    region='us-west-2',
    ami='ami-1cdd532c',
    key_name='ben-datadesk',
    instance_type='m1.medium',
    block_gb_size=12
):
    """
    Spin up a new server on Amazon EC2.

    Returns the id and public address.

    By default, we use Ubuntu 12.04 LTS
    """
    print("Warming up...")
    conn = boto.ec2.connect_to_region(
        region,
        aws_access_key_id=env.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=env.AWS_SECRET_ACCESS_KEY,
    )
    print("Reserving an instance...")
    bdt = boto.ec2.blockdevicemapping.BlockDeviceType(connection=conn)
    bdt.size = block_gb_size
    bdm = boto.ec2.blockdevicemapping.BlockDeviceMapping(connection=conn)
    bdm['/dev/sda1'] = bdt
    reservation = conn.run_instances(
        ami,
        key_name=key_name,
        instance_type=instance_type,
        block_device_map=bdm,
    )
    instance = reservation.instances[0]
    print('Waiting for instance to start...')
    # Check up on its status every so often
    status = instance.update()
    while status == 'pending':
        time.sleep(10)
        status = instance.update()
    if status == 'running':
        print('New instance %s' % instance.id)
        print('Accessible at %s' % instance.public_dns_name)
    else:
        print('Instance status: ' + status)
    return (instance.id, instance.public_dns_name)
