import argparse
import re
import sys

from ics import Calendar
from ics import Event

diningcity_sms_re = re.compile(
    r"预订成功，(?P<time>\d{4}-\d{2}-\d{2} \d{2}:\d{2})于(?P<name>.+?)(?P<num>\d+)位。"
)


def create_ics(text: str) -> Calendar:
    c = Calendar()
    for match in diningcity_sms_re.findall(text):
        date, resturant, num_people = match
        event = Event()
        event.name = f"{resturant.strip()} {num_people}位"
        event.location = resturant.strip()
        event.begin = f"{date}:00+08:00"
        event.duration = {"hours": 2}
        c.events.add(event)
    return c


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input",
        type=str,
        nargs=argparse.OPTIONAL,
        help="path to read input. default to stdin",
    )
    parser.add_argument("output", type=str, help="path to write generated ics file")
    args = parser.parse_args()
    input = open(args.input, "w") if args.input else sys.stdin
    text = input.read().strip()
    calendar = create_ics(text)
    with open(args.output, "w") as f:
        f.writelines(calendar)


if __name__ == "__main__":
    main()
