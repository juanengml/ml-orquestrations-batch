from jobs import (
 job_automation_turn_off_office_one,
 job_automation_turn_on_office_one,
 job_automation_turn_off_luz_garagem,
 job_automation_turn_on_luz_garagem,
 job_automation_turn_on_luz_rede,
 job_automation_turn_off_luz_rede,
 job_automation_turn_on_luz_quartinho,
 job_automation_turn_off_luz_quartinho
)

from plombery import Trigger, register_pipeline
from apscheduler.triggers.cron import CronTrigger




register_pipeline(
    id="job_automation_turn_on_luz_quartinho",
    description="Turn on the lights at 08:30",
    tasks=[job_automation_turn_on_luz_quartinho],
    triggers=[
        Trigger(
            id="daily_evening",
            name="Daily Evening",
            description="Run the pipeline every day at 08:30",
            schedule=CronTrigger(hour=8, minute=30),
        ),
    ],
)

register_pipeline(
    id="job_automation_turn_off_luz_quartinho",
    description="Turn on the lights at 20:30",
    tasks=[job_automation_turn_off_luz_quartinho],
    triggers=[
        Trigger(
            id="daily_evening",
            name="Daily Evening",
            description="Run the pipeline every day at 20:30 ",
            schedule=CronTrigger(hour=20, minute=30),
        ),
    ],
)



register_pipeline(
    id="job_automation_turn_on_luz_rede",
    description="Turn on the lights at 17:30",
    tasks=[job_automation_turn_on_luz_rede],
    triggers=[
        Trigger(
            id="daily_evening",
            name="Daily Evening",
            description="Run the pipeline every day at 17:30",
            schedule=CronTrigger(hour=17, minute=30),
        ),
    ],
)

register_pipeline(
    id="job_automation_turn_off_luz_rede",
    description="Turn on the lights at 8:30",
    tasks=[job_automation_turn_off_luz_rede],
    triggers=[
        Trigger(
            id="daily_evening",
            name="Daily Evening",
            description="Run the pipeline every day at 8:30 ",
            schedule=CronTrigger(hour=8, minute=30),
        ),
    ],
)



register_pipeline(
    id="job_automation_turn_off_luz_garagem",
    description="Turn off the lights at 08:30  every day",
    tasks=[job_automation_turn_off_luz_garagem],
    triggers=[
        Trigger(
            id="daily_evening",
            name="Daily Evening",
            description="Run the pipeline every day at 08:30 ",
            schedule=CronTrigger(hour=8, minute=30),
        ),
    ],
)

register_pipeline(
    id="job_automation_turn_on_luz_garagem",
    description="Turn on the lights at 17:30  every day",
    tasks=[job_automation_turn_on_luz_garagem],
    triggers=[
        Trigger(
            id="daily_evening",
            name="Daily Evening",
            description="Run the pipeline every day at 17:30 ",
            schedule=CronTrigger(hour=17, minute=30),
        ),
    ],
)


register_pipeline(
    id="job_automation_turn_on_office_one",
    description="Turn on the lights at 17:30  every day",
    tasks=[job_automation_turn_on_office_one],
    triggers=[
        Trigger(
            id="daily_evening",
            name="Daily Evening",
            description="Run the pipeline every day at 17:30 ",
            schedule=CronTrigger(hour=17, minute=30),
        ),
    ],
)


register_pipeline(
    id="job_automation_turn_off_office_one",
    description="Turn off the lights at 23:00  every day",
    tasks=[job_automation_turn_off_office_one],
    triggers=[
        Trigger(
            id="daily_evening",
            name="Daily Evening",
            description="Run the pipeline every day at 23:00 ",
            schedule=CronTrigger(hour=23, minute=00),
        ),
    ],
)





if __name__ == "__main__":
    import uvicorn

    uvicorn.run("plombery:get_app", reload=True, factory=True, host="0.0.0.0", port=8001)
