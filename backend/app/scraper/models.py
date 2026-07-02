from dataclasses import dataclass


@dataclass
class Assessment:

    name: str

    url: str

    description: str

    test_type: str

    duration: str

    remote_testing: bool

    adaptive: bool

    languages: list[str]

    job_levels: list[str]

    skills: list[str]