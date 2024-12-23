import asyncio
import json
from datetime import datetime

import flet as ft
import websockets

from components import get_match_card

leagues_events = {}


async def websocket_client(page):
    uri = "ws://localhost:8764"
    try:
        async with websockets.connect(uri) as websocket:
            while True:
                message = await websocket.recv()
                message = json.loads(message)
                print(f"Received message: {message}")
                # Update the Flet UI with the received message
                update_events(message, page)
                update_components(page)
                page.update()
                await asyncio.sleep(1)
    except Exception as e:
        print(f"WebSocket error: {e}")


class LeagueEvents:
    SHOW_MORE_COUNT = 10
    SHOW_LESS_COUNT = 3

    def __init__(self, league, page):
        self.league = league
        self.events = []
        self.is_show_more = False

        # Global ctx to updated page after click on show more btn
        self.page = page

    def add_event(self, event):
        self.events.append(event)
        self.events = sorted(self.events,
                             key=lambda x: x["end_datetime"],
                             reverse=True)

    def get_visible_events(self):
        if self.is_show_more:
            return self.events[:LeagueEvents.SHOW_MORE_COUNT]
        else:
            return self.events[:LeagueEvents.SHOW_LESS_COUNT]

    def update_show_more(self, u):
        self.is_show_more = u
        print(f"Show more btn: {self.is_show_more}")
        update_components(self.page)
        self.page.update()

    def get_section(self):
        league_section = ft.Column(key=self.league)
        league_header = ft.Text(self.league, size=20, weight=ft.FontWeight.BOLD)
        match_cards = [get_match_card(ev) for ev in self.get_visible_events()]
        league_section.controls = [league_header] + match_cards
        if self.is_show_more:
            b = ft.ElevatedButton(text="Show Less", on_click=lambda e: self.update_show_more(False))
        else:
            b = ft.ElevatedButton(text="Show More", on_click=lambda e: self.update_show_more(True))
        league_section.controls.append(b)
        return league_section


def update_events(message, page):
    league = message["league"]
    end_timestamp = message["end_timestamp"] / 1000  # Convert milliseconds to seconds
    message["end_datetime"] = datetime.fromtimestamp(end_timestamp).strftime('%d/%m/%y : %H:%M')
    if league not in leagues_events:
        leagues_events[league] = LeagueEvents(league, page)
    leagues_events[league].add_event(message)


def update_components(page):
    # Ensure the ListView and its content are initialized
    if not page.controls:
        list_view = ft.ListView(
            expand=True,
            spacing=10,
            padding=20,
            auto_scroll=False
        )
        page.controls.append(list_view)
    league_controls = [league.get_section() for league in leagues_events.values()]
    page.controls[0].controls = league_controls


async def main(page: ft.Page):
    page.title = "WebSocket Client"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Start the WebSocket client
    await asyncio.create_task(websocket_client(page))
    # await page.update_async()


if __name__ == "__main__":
    # Start the Flet client
    ft.app(target=main, view=ft.WEB_BROWSER)
