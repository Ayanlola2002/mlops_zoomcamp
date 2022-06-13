from prefect.deployments import DeploymentSpec
from prefect.orion.schemas.schedules import CronSchedule


DeploymentSpec(
    name="cron-schedule-deployment-daniel",
    flow_location="/home/ayanlola/my_mlops_zoomcamp/workflow_orchestration_week_3",
    schedule=CronSchedule(cron="0 9 15 * *"),
    tags=['flow_test_tuna_cron']
)