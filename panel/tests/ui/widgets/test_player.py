import pytest

pytest.importorskip("playwright")

from playwright.sync_api import expect

from panel.tests.util import serve_component, wait_until
from panel.widgets import Player

pytestmark = pytest.mark.ui


def test_player_visible_buttons(page):
    player = Player(visible_buttons=["play", "pause"])
    serve_component(page, player)

    assert page.is_visible(".play")
    assert page.is_visible(".pause")
    assert not page.is_visible(".reverse")
    assert not page.is_visible(".first")
    assert not page.is_visible(".previous")
    assert not page.is_visible(".next")
    assert not page.is_visible(".last")
    assert not page.is_visible(".slower")
    assert not page.is_visible(".faster")

    player.visible_buttons = ["first"]
    wait_until(lambda: page.is_visible(".first"))
    assert not page.is_visible(".play")
    assert not page.is_visible(".pause")


def test_player_visible_loop_options(page):
    player = Player(visible_loop_options=["loop", "once"])
    serve_component(page, player)

    assert page.is_visible(".loop")
    assert page.is_visible(".once")
    assert not page.is_visible(".reflect")

    player.visible_loop_options = ["reflect"]
    wait_until(lambda: page.is_visible(".reflect"))
    assert not page.is_visible(".loop")
    assert not page.is_visible(".once")


def test_player_scale_buttons(page):
    player = Player(scale_buttons=2)
    serve_component(page, player)

    expect(page.locator(".play")).to_have_attribute(
        "style",
        "text-align: center; flex-grow: 2; margin: 2px; transform: scale(2); max-width: 50px;",
    )
