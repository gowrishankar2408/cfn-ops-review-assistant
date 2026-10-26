from cfn_ops_review_assistant.cli import app


def test_main_returns_to_menu_after_review(monkeypatch):
    selections = iter([("psr-review", "123"), None])
    menu_calls = 0
    reviews = []

    def show_menu():
        nonlocal menu_calls
        menu_calls += 1
        return next(selections)

    monkeypatch.setattr(app, "show_menu", show_menu)
    monkeypatch.setattr(
        app,
        "_run_review",
        lambda review_type, case_number: reviews.append(
            (review_type, case_number)
        ) or 0,
    )

    assert app.main([]) == 0
    assert menu_calls == 2
    assert reviews == [("psr-review", "123")]