#!/usr/bin/env python3
"""Generate the PDF drawing operators for the Silo emblem on the title page.

The emblem is a ring of twelve citizens standing hand in hand, their heads
outward and their feet meeting at the centre, enclosed by a line that runs
round them at two different radii and steps between the two with a square
corner, twice.

It is drawn with raw PDF path operators emitted by \\pdfliteral, because this
machine has no tikz, no pict2e and no metafont, and because an emblem that
lives in the source rather than in a binary file stays readable and diffable.

Run from the repository root:

    python3 tools/mkemblem.py

and paste the single line it prints into the definition of \\pact@emblemink in
book/pact.sty.  Nothing in the build calls this script; it is the record of
how the numbers were arrived at, and the way to change them.

All coordinates are in PostScript points, with the origin at the centre.  The
emblem is drawn once at a nominal size and \\siloemblem scales it.
"""

import math

# --- the enclosing line ----------------------------------------------------
R_IN = 38.0           # the radius it keeps round the upper left
R_OUT = 46.5          # the radius it keeps round the lower right
RING_W = 1.7
JOG_TOP = 95.0        # where it steps outward, degrees counter-clockwise
JOG_BOT = 232.0       # where it steps back in

# --- one citizen -----------------------------------------------------------
# Measured off the prop as fractions of R_IN and converted here.  Heads point
# outward; the feet of neighbouring citizens meet and leave a twelve-pointed
# star open at the centre.
HIP_R = 19.0          # radius at which the hips sit
TRUNK = 6.0           # hip to shoulder
ARM_X, ARM_Y = 6.2, 4.0   # shoulder to hand, sideways and outward
LEG_X, LEG_Y = 1.7, 10.6  # hip to foot, sideways and inward
HEAD_DY, HEAD_R = 4.9, 2.4  # shoulder to head centre; head radius
LIMB_W = 1.8          # stroke width of a limb
COUNT = 12


def circle(cx, cy, r):
    """A closed circle as four Bezier arcs."""
    k = 0.5522847498 * r
    return (
        f"{cx:.2f} {cy + r:.2f} m "
        f"{cx + k:.2f} {cy + r:.2f} {cx + r:.2f} {cy + k:.2f} {cx + r:.2f} {cy:.2f} c "
        f"{cx + r:.2f} {cy - k:.2f} {cx + k:.2f} {cy - r:.2f} {cx:.2f} {cy - r:.2f} c "
        f"{cx - k:.2f} {cy - r:.2f} {cx - r:.2f} {cy - k:.2f} {cx - r:.2f} {cy:.2f} c "
        f"{cx - r:.2f} {cy + k:.2f} {cx - k:.2f} {cy + r:.2f} {cx:.2f} {cy + r:.2f} c h "
    )


def arc(r, a0, a1, move=True):
    """An arc of radius r from a0 to a1 degrees, counter-clockwise, in Bezier
    segments of no more than ninety degrees apiece."""
    a0, a1 = math.radians(a0), math.radians(a1)
    while a1 < a0:
        a1 += 2 * math.pi
    n = max(1, int(math.ceil((a1 - a0) / (math.pi / 2))))
    step = (a1 - a0) / n
    k = 4.0 / 3.0 * math.tan(step / 4.0)
    out = []
    if move:
        out.append(f"{r * math.cos(a0):.2f} {r * math.sin(a0):.2f} m ")
    for i in range(n):
        t0 = a0 + i * step
        t1 = t0 + step
        x0, y0 = r * math.cos(t0), r * math.sin(t0)
        x1, y1 = r * math.cos(t1), r * math.sin(t1)
        c0 = (x0 - k * r * math.sin(t0), y0 + k * r * math.cos(t0))
        c1 = (x1 + k * r * math.sin(t1), y1 - k * r * math.cos(t1))
        out.append(f"{c0[0]:.2f} {c0[1]:.2f} {c1[0]:.2f} {c1[1]:.2f} {x1:.2f} {y1:.2f} c ")
    return "".join(out)


def jog(angle, r_from, r_to):
    """The square corner by which the line steps from one radius to the other:
    out along one axis, then across on the other, so that it turns a right
    angle rather than running straight down a radius."""
    a = math.radians(angle)
    x0, y0 = r_from * math.cos(a), r_from * math.sin(a)
    x1, y1 = r_to * math.cos(a), r_to * math.sin(a)
    if abs(math.sin(a)) >= abs(math.cos(a)):
        corner = (x0, y1)          # go up or down first, then across
    else:
        corner = (x1, y0)          # go out sideways first, then up or down
    return f"{corner[0]:.2f} {corner[1]:.2f} l {x1:.2f} {y1:.2f} l "


def ring():
    out = [f"{RING_W:.2f} w "]
    out.append(arc(R_IN, JOG_TOP, JOG_BOT))
    out.append(jog(JOG_BOT, R_IN, R_OUT))
    out.append(arc(R_OUT, JOG_BOT, JOG_TOP + 360.0, move=False))
    out.append(jog(JOG_TOP, R_OUT, R_IN))
    out.append("S ")
    return "".join(out)


def figure():
    """One citizen, in her own frame: +y points outward, origin at the hips."""
    sh = TRUNK
    out = []
    out.append(f"0 0 m 0 {sh:.2f} l S ")
    out.append(f"0 {sh:.2f} m {ARM_X:.2f} {sh + ARM_Y:.2f} l S ")
    out.append(f"0 {sh:.2f} m {-ARM_X:.2f} {sh + ARM_Y:.2f} l S ")
    out.append(f"0 0 m {LEG_X:.2f} {-LEG_Y:.2f} l S ")
    out.append(f"0 0 m {-LEG_X:.2f} {-LEG_Y:.2f} l S ")
    out.append(circle(0, sh + HEAD_DY, HEAD_R) + "f ")
    return "".join(out)


def emblem():
    out = ["q 1 J 1 j "]                      # round caps, round joins
    out.append(ring())
    out.append(f"{LIMB_W:.2f} w ")
    fig = figure()
    for i in range(COUNT):
        t = math.radians(i * 360.0 / COUNT)
        c, s = math.cos(t), math.sin(t)
        out.append(
            f"q {c:.5f} {s:.5f} {-s:.5f} {c:.5f} "
            f"{-s * HIP_R:.3f} {c * HIP_R:.3f} cm {fig}Q "
        )
    out.append("Q")
    return "".join(out)


if __name__ == "__main__":
    print(emblem())
