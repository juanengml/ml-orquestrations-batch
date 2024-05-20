from jobs import (
    job_submit_extract_address_data,
    job_submit_extract_beer_data,
    job_submit_extract_cripto_data,
    job_submit_extract_company_data,
    job_submit_ml_adeline,
    job_automation_turn_on,
    job_automation_turn_off
)
from apscheduler.triggers.interval import IntervalTrigger
from plombery import Trigger, register_pipeline
from apscheduler.triggers.cron import CronTrigger


register_pipeline(
    id="job_submit_ml_adeline",
    description="Aggregate sales activity from all stores across the country",
    tasks=[job_submit_ml_adeline],
    triggers=[
        Trigger(
            id="daily",
            name="Daily",
            description="Run the pipeline every day",
            schedule=IntervalTrigger(minutes=120),
        ),
    ],
)



register_pipeline(
    id="job_submit_extract_address_data",
    description="Aggregate sales activity from all stores across the country",
    tasks=[job_submit_extract_address_data],
    triggers=[
        Trigger(
            id="daily",
            name="Daily",
            description="Run the pipeline every day",
            schedule=IntervalTrigger(minutes=10),
        ),
    ],
)

register_pipeline(
    id="job_submit_extract_beer_data",
    description="Aggregate sales activity from all stores across the country",
    tasks=[job_submit_extract_beer_data],
    triggers=[
        Trigger(
            id="daily",
            name="Daily",
            description="Run the pipeline every day",
            schedule=IntervalTrigger(minutes=60),
        ),
    ],
)

register_pipeline(
    id="job_submit_extract_cripto_data",
    description="Aggregate sales activity from all stores across the country",
    tasks=[job_submit_extract_cripto_data],
    triggers=[
        Trigger(
            id="daily",
            name="Daily",
            description="Run the pipeline every day",
            schedule=IntervalTrigger(minutes=40),
        ),
    ],
)

register_pipeline(
    id="job_submit_extract_company_data",
    description="Aggregate sales activity from all stores across the country",
    tasks=[job_submit_extract_company_data],
    triggers=[
        Trigger(
            id="daily",
            name="Daily",
            description="Run the pipeline every day",
            schedule=IntervalTrigger(minutes=50),
        ),
    ],
)


register_pipeline(
    id="job_automation_turn_on",
    description="Turn on the lights at 06:00 PM every day",
    tasks=[job_automation_turn_on],
    triggers=[
        Trigger(
            id="daily_evening",
            name="Daily Evening",
            description="Run the pipeline every day at 17:30 PM",
            schedule=CronTrigger(hour=17, minute=30),
        ),
    ],
)

register_pipeline(
    id="lights_off",
    description="Turn off the lights at 07:00 AM every day",
    tasks=[job_automation_turn_off],
    triggers=[
        Trigger(
            id="daily_morning",
            name="Daily Morning",
            description="Run the pipeline every day at 07:00 AM",
            schedule=CronTrigger(hour=7, minute=0),
        ),
    ],
)



if __name__ == "__main__":
    import uvicorn

    uvicorn.run("plombery:get_app", reload=True, factory=True, host="0.0.0.0", port=8000)
