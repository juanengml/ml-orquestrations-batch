from jobs import (
    job_automation_turn_on,
    job_automation_turn_off,
    job_automation_turn_off_office_one,
    job_automation_turn_on_office_one
)
from apscheduler.triggers.interval import IntervalTrigger
from plombery import Trigger, register_pipeline
from apscheduler.triggers.cron import CronTrigger


register_pipeline(
    id="job_automation_turn_off_office_one",
    description="Turn on the lights at 17:30 PM every day",
    tasks=[job_automation_turn_off_office_one],
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
    id="job_automation_turn_on_office_one",
    description="Turn on the lights at 23:00 PM every day",
    tasks=[job_automation_turn_on_office_one],
    triggers=[
        Trigger(
            id="daily_evening",
            name="Daily Evening",
            description="Run the pipeline every day at 23:00 PM",
            schedule=CronTrigger(hour=23, minute=00),
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
    id="job_automation_turn_off",
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

    uvicorn.run("plombery:get_app", reload=True, factory=True, host="0.0.0.0", port=8001)
