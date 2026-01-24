import reflex as rx
from rxconfig import config

def link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, 
                size="4",
                style = {"color": "#ffffff"},
                ),
        href=url,
        is_external=True,
    )
    
def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.image(
                    src="/images/logo.jpg",
                    width="2.25em",
                    height="auto",
                    border_radius="25%",
                ),
                rx.heading("NOCT",
                            size="7",
                            font_family="Nasalisation",
                            letter_spacing="0.02em",
                            ),
                align_items="center",
            ),
            rx.hstack(
                link("Home", url="https://noct.com"),
                link("Recordings", url="https://youtube.com/@noctspace/"),
                link("Join", url="https://discord.gg/heMBuNu7kt/"),
                justify="end",
                spacing="7",
                display=["none", "none", "flex"],
            ),
            rx.menu.root(
                rx.menu.trigger(
                  rx.button(
                    rx.icon("menu"),
                    variant="ghost",
                    size="3",  
                  ),  
                ),
                rx.menu.content(
                    rx.menu.item(link("Home", url="https://noct.com"),),
                    rx.menu.item(link("Recordings", url="https://youtube.com/@noctspace/"),),
                    rx.menu.item(link("Join", url="https://discord.gg/heMBuNu7kt/"),),
                    display=["block", "block", "none"],
                ),
                justify="between",
                align_items="center",
            ),
            justify="between",
            align_items="center",
        ),
        padding="1em",
        top="0px",
        z_index="5",
        width="100%",
        style={
            "background": "rgba(255, 255, 255, 0.08)",
            "backdropFilter": "blur(20px), saturate(120%)",
            "WebkitBackdropFilter": "blur(20px), saturate(120%)",
        },
    )
    
def stars():
    return rx.fragment(
        rx.el.canvas(
            id="stars",
            position="fixed",
            inset="0",
            z_index="-1",
        ),
        rx.script("""
            (function initStars() {
            const canvas = document.getElementById("stars");
            if (!canvas) {
                requestAnimationFrame(initStars);
                return;
            }

            const ctx = canvas.getContext("2d");

            function resize() {
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
            }
            resize();
            window.addEventListener("resize", resize);

            const STAR_COUNT = 900;
            const stars = Array.from({ length: STAR_COUNT }, () => {
                const z = Math.random();
                const rarity = Math.pow(Math.random(), 3)
                
                let hue;
                if (rarity < 0.015) hue = 285;
                else if (rarity < 0.04) hue = 190;
                else if (rarity < 0.10) hue = 45;
                else if (rarity < 0.25) hue = 15;
                else hue = 200 + Math.random() * 40;
                
                return {
                x: Math.random(),
                y: Math.random(),
                z,
                hue,
                sat: 40 + Math.random() * 50,
                light: 60 + z * 30,
                size: 0.6 + Math.pow(z, 1.5) * 2.2,
                glow: Math.pow(z, 2) * 18,
                twinkle: Math.random() * 0.6 + 0.2,
                };
            });

            let targetX = 0, targetY = 0;
            let mx = 0, my = 0;

            window.addEventListener("mousemove", e => {
                const rect = canvas.getBoundingClientRect();
                
                targetX = ((e.clientX - rect.left) / rect.width - 0.5) * 2;
                targetY = ((e.clientY - rect.top) / rect.height - 0.5) * 2;
            });

            function draw() {
                mx += (targetX - mx) * 0.05;
                my += (targetY - my) * 0.05;

                ctx.clearRect(0, 0, canvas.width, canvas.height);
                
                const t = performance.now() * 0.001;

                for (const s of stars) {
                const d = s.z * 0.85 + 0.15;
                
                const x = (s.x + mx * 0.12 * d) * canvas.width;
                const y = (s.y + my * 0.12 * d) * canvas.height;
                
                const tw = Math.sin(t * s.twinkle + s.x * 20) * 0.15;
                const r = (s.size + tw) * d;

                ctx.fillStyle = `hsla(${s.hue}, ${s.sat}%, ${s.light}%, 1)`;
                ctx.shadowColor = `hsla(${s.hue}, ${s.sat}%, ${s.light + 10}%, 0.9)`;
                ctx.shadowBlur = s.glow * d;

                ctx.beginPath();
                ctx.arc(x, y, r, 0, Math.PI * 2);
                ctx.fill();
                }

                requestAnimationFrame(draw);
            }

            draw();
            })();
        """,
        defer=True,
        ),
    )

def heroScroll():
    return rx.script(
        """
        (function heroScroll() {
            const root = document.documentElement;
            
            function onScroll() {
                const max = window.innerHeight * 0.7;
                const y = Math.min(window.scrollY, max);
                const t = y / max;
                const eased = 1 - Math.pow(1 - t, 3);
                
                root.style.setProperty("--scroll", eased.toFixed(3));
            }
            
            window.addEventListener("scroll", onScroll);
            onScroll();
        })();
        """,
        defer=True,
    ),
    
def content() -> rx.Component:
    return rx.box(
                rx.flex(
                    rx.box(height="35vh"),
                    rx.text(
                        "NOCT",
                        style={
                            "color": "#ffffff",
                            "font_size": "clamp(10rem, 40vw, 50rem)",
                            "font_weight": "200",
                            "font_family": "Nasalisation",
                            "letter_spacing": "0.02em",
                            "text_align": "center",
                            "font_stretch": "expanded",
                            "opacity": "calc(0.6 + var(--scroll, 0) * 0.4)",
                            "line_height": "0.8",
                            "filter": "blur(calc((1 - var(--scroll, 0)) * 2px))",
                        },
                    ),
                    rx.box(height="10vh"),
                    rx.flex(
                        rx.desktop_only(
                            rx.box(
                                rx.image(
                                    src="/images/apollo.png",
                                    style={
                                        "position": "absolute",
                                        "top": "0",
                                        "left": "0",
                                        "width": "90%",
                                        "z_index": "1",
                                        "transition": "transform 0.3s ease, filter 0.3s ease",
                                        "_hover": {
                                          "transform": "scale(1.05)",
                                          "filter": "brightness(1.2)"  
                                        },
                                    },
                                ),
                                rx.image(
                                    src="images/kepler.png",
                                    style={
                                        "position": "absolute",
                                        "top": "35%",
                                        "left": "0",
                                        "width": "70%",
                                        "z_index": "2",
                                        "transition": "transform 0.3s ease, filter 0.3s ease",
                                        "_hover": {
                                          "transform": "scale(1.05)",
                                          "filter": "brightness(1.2)"  
                                        },
                                    },
                                ),
                                rx.image(
                                    src="images/disk.png",
                                    style={
                                        "position": "absolute",
                                        "top": "35%",
                                        "left": "35%",
                                        "width": "70%",
                                        "z_index": "3",
                                        "transition": "transform 0.3s ease, filter 0.3s ease",
                                        "_hover": {
                                          "transform": "scale(1.05)",
                                          "filter": "brightness(1.2)"  
                                        },
                                    },
                                ),
                                position="relative",
                                width="clamp(260px, 40vw, 420px)",
                                height="clamp(260px, 40vw, 420px)",
                            ),
                        ),
                        rx.text(
                            "High school led astronomy colloquium series featuring talks\n from leading PhD researchers",
                            style={
                                "color": "#ffffff",
                                "position": "relative",
                                "pointer_events": "none",
                                "text_align": "center",
                                "font_size": "clamp(1rem, 1.2vw + 0.5rem, 1.75rem)",
                                "font_weight": "400",
                                "font_family": "sans-serif",
                                "letter_spacing": "0.15em",
                                "max_width": "35ch",
                                "margin_x": "auto",
                            }
                        ),
                        rx.desktop_only(
                            rx.box(
                                rx.image(
                                    src="images/sputnik.png",
                                    style={
                                        "position": "absolute",
                                        "top": "10%",
                                        "left": "0",
                                        "width": "60%",
                                        "z_index": "1",
                                        "transition": "transform 0.3s ease, filter 0.3s ease",
                                        "_hover": {
                                          "transform": "scale(1.05)",
                                          "filter": "brightness(1.2)"  
                                        },
                                    },
                                ),
                                rx.image(
                                    src="images/starship.png",
                                    style={
                                        "position": "absolute",
                                        "top": "0",
                                        "left": "10%",
                                        "z_index": "2",
                                        "transition": "transform 0.3s ease, filter 0.3s ease",
                                        "_hover": {
                                          "transform": "scale(1.05)",
                                          "filter": "brightness(1.2)"  
                                        },   
                                    },    
                                ),
                                rx.image(
                                    src="images/telescope.png",
                                    style={
                                    "position": "absolute",
                                    "top": "30%",
                                    "left": "-20%",
                                    "z_index": "3",
                                    "transition": "transform 0.3s ease, filter 0.3s ease",
                                    "_hover": {
                                          "transform": "scale(1.05)",
                                          "filter": "brightness(1.2)"  
                                    },  
                                    },
                                ),
                                position="relative",
                                display={
                                "initial": "none",
                                "sm": "block",
                                },
                                width="clamp(260px, 40vw, 420px)",
                                height="clamp(260px, 40vw, 420px)"
                            ),
                        ),
                        style={
                            "opacity": "calc(clamp(0, (var(--scroll, 0) - 0.5) * 4, 1) * (0.6 + var(--scroll, 0) * 0.4))",
                        },
                        direction="row",
                        spacing="5",
                        align="center",
                        justify="center",
                    ),
                    rx.box(height="20vh"),
                    rx.box(
                        rx.text(
                            "Past Speakers From",
                            style={
                                "color": "#ffffff",
                                "font_size": "clamp(2rem, 2.5vw + 1rem, 3.5rem)",
                                "font_weight": "400",
                                "font_family": "sans-serif",
                                "align": "center",
                                "justify": "center",
                            }
                        ),
                        rx.box(height="5vh"),
                        rx.flex(
                            rx.image(src="images/logos/mit.png", height="100px", width="auto", object_fit="contain",),
                            rx.image(src="images/logos/Harvard.svg", height="100px", width="auto", object_fit="contain",),
                            rx.image(src="images/logos/ligo.png", height="100px", width="auto", object_fit="contain",),
                            rx.image(src="images/logos/cmu.avif", height="100px", width="auto", object_fit="contain",),
                            rx.image(src="images/logos/uofedinburgh.png", height="100px", width="auto", object_fit="contain",),
                            rx.image(src="images/logos/uofvirginia.png", height="100px", width="auto", object_fit="contain",),
                            direction="row",
                            wrap="wrap",
                            spacing="9",
                            align="center",
                            justify="center",
                        ),
                        style={"text_align": "center",},
                        width="100%",   
                    ),
                    direction="column",
                    align="center",
                    spacing="6",
                    width="100%",
                ),
                rx.image(
                    src="/images/astronaut.png",
                    style={
                        "position": "fixed",
                        "bottom": "0",
                        "left": "50%",
                        "height": "clamp(300px, 40vw, 50rem)",
                        "transform": (
                            "translateX(-50%) "
                            "translateY(calc(var(--scroll, 0) * 32px))"
                            ),
                        "opacity": "calc(1 - min(var(--scroll, 0) * 1.2, 1))",
                        "filter": "blur(calc(min(var(--scroll, 0) * 2.4, 1) * 8px))",
                    },
                ),
                rx.box(height="20vh"),
                position="relative",
                width="100%",
                height="100%",
                overflow_x="hidden",
            ),
    

def index() -> rx.Component:
    return rx.box(
        stars(),
        heroScroll(),
        rx.vstack(
            navbar(),
            content(),
            inset="0",
            z_index="1",
            background_color="transparent",
            width="100%",
        ),
        width="100%",
    )


app = rx.App(
    style = {
        "html, body, #root":{
            "height": "100%",
            "width": "100%",
            "margin": "0",
            "padding": "0",
            "background_color": "black",
        },
        "::selection": {"background_color": "#4e8cff"},
    },
    theme = rx.theme(
        breakpoints=["520px", "768px", "1024px", "1280px", "1640px"],
    ),
    stylesheets=["/fonts.css", "scrollbar.css"]
)

app.add_page(index, title="NOCT")