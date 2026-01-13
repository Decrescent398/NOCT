import reflex as rx
from rxconfig import config

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, 
                size="4",
                style = {"color": "#ffffff"},
                ),
        href=url,
    )
    
def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
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
                    navbar_link("Home", "/#"),
                    navbar_link("About", "/#"),
                    navbar_link("Recordings", "/#"),
                    navbar_link("Join", "/#"),
                    justify="end",
                    spacing="7",
                ),
                justify="between",
                align_items="center",
            ),
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
    

def index() -> rx.Component:
    return rx.box(
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
        defer=True,),
        rx.vstack(
            navbar(),
            rx.box(
                rx.text(
                    "NOCT",
                    style={
                        "color": "#ffffff",
                        "font_size": "clamp(10rem, 40vw, 50rem)",
                        "font_weight": "20",
                        "font_family": "Nasalisation",
                        "letter_spacing": "0.02em",
                        "text_align": "center",
                        "font_stretch": "expanded",
                    },
                ),
                rx.image(
                    src="/images/astronaut.png",
                    style={
                        "position": "absolute",
                        "bottom": "0",
                        "left": "50%",
                        "height": "clamp(300px, 40vw, 50rem)",
                        "transform": "translateX(-50%)",
                    },
                ),
                position="relative",
                width="100%",
                height="100%",
            ),
            position="fixed",
            inset="0",
            z_index="1",
            background_color="transparent",
        ),
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
    stylesheets=["/fonts.css"]
)

app.add_page(index, title="NOCT")