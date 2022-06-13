from prefect.deployments import DeploymentSpec
from prefect.orion.schemas.schedules import CronSchedule


DeploymentSpec(
    name="cron-schedule-deployment-ayanlola",
    flow_location="/home/ayanlola/my_mlops_zoomcamp/workflow_orchestration_week_3",
    schedule=CronSchedule(cron="0 9 15 * *"),
    tags=['flow_test_ayanlola_cron']
)