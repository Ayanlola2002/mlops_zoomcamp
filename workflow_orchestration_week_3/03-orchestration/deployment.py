from prefect.deployments import DeploymentSpec
from prefect.orion.schemas.schedules import CronSchedule
from prefect.flow_runners import SubprocessFlowRunner


DeploymentSpec(
    name="cron-schedule-deployment-ayanlola",
    flow_runner=SubprocessFlowRunner(),
    flow_location="/home/ayanlola/my_mlops_zoomcamp/workflow_orchestration_week_3/03-orchestration/homework.py",
    schedule=CronSchedule(cron="0 9 15 * *"),
    tags=['flow_test_ayanlola_cron']
)