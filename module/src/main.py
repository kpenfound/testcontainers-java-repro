import dagger
from dagger.mod import function


@function
def test_containers(dir: dagger.Directory) -> dagger.Container:
    # Example usage: "dagger call container-echo --string-arg hello"
    return dagger.testcontainers().enable(dagger.container().from_("maven:3.9-amazoncorretto-21-al2023")).with_directory("/src", dir).with_workdir("/src").with_exec(["mvn", "test"])

