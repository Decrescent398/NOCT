import reflex as rx

config = rx.Config(
    app_name="noct_app",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
    show_built_with_reflex=False,
    enable_state=False,
)