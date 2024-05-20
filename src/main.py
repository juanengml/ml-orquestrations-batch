from jobs import (
    job_submit_extract_address_data,
    job_submit_extract_beer_data,
    job_submit_extract_cripto_data,
    job_submit_extract_company_data,
    job_submit_ml_adeline
)
from apscheduler.triggers.interval import IntervalTrigger
from plombery import Trigger, register_pipeline


register_pipeline(
    id="job_submit_ml_adeline",
    description="Aggregate sales activity from all stores across the country",
    tasks=[job_submit_ml_adeline],
    triggers=[
        Trigger(
            id="daily",
            name="Daily",
            description="Run the pipeline every day",
            schedule=IntervalTrigger(minutes=5),
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
            schedule=IntervalTrigger(minutes=5),
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
            schedule=IntervalTrigger(minutes=5),
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
            schedule=IntervalTrigger(minutes=5),
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
            schedule=IntervalTrigger(minutes=5),
        ),
    ],
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("plombery:get_app", reload=True, factory=True, host="0.0.0.0", port=8000)
