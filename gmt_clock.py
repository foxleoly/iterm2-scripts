#!/usr/bin/env python3

import iterm2
import datetime

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description="GMT Clock",
        detailed_description="Shows the time in jolly old England",
        knobs=[],
        exemplar="[12:00 GMT]",
        update_cadence=1,
        identifier="com.iterm2.example.gmt-clock")

    # This function gets called once per second.
    @iterm2.StatusBarRPC
    async def coro(knobs):
        return datetime.datetime.now().strftime("%H:%M:%S GMT")

    # Register the component.
    await component.async_register(connection, coro)

iterm2.run_forever(main)
