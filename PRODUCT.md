# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Primary: senior leadership and C-suite executives at corporations and industry
bodies, plus the conference and event organizers who buy on their behalf. They
arrive with a complex body of material — a strategy, a launch, a year of
research, an industry position — and a fixed moment in which it has to land with
an audience that will not read a deck twice.

They are evaluating whether this person can be trusted with a high-stakes,
high-visibility moment. They are typically comparing against agencies and
in-house teams, and they are not shopping on price.

## Product Purpose

An independent information-architecture practice, presented publicly as three
tiers, ordered flagship-first so the largest engagement anchors the rest:

1. **Live Events** — on site: presentation design and information architecture,
   plus substantial rehearsal time with senior leadership. Presence is the
   differentiator and the main cost driver. Covers the underlying Presentation
   Design, Information Management and Event Planning services.
2. **Strategy & Content** — advisory, not production: research, review of the
   client's existing material and talk, and rehearsals, run on the client's
   schedule and in whatever format suits them. **Nothing is designed or built
   in this tier** — the output is direction and a plan. Covers Content Strategy
   and Strategic Planning.
3. **Speaking & Training** — keynotes, and in-company workshops for sales and
   training teams, aimed at leaving them able to work without him. The quickest
   engagements to sell. Covers Public Speaking and Corporate Training.

Tiers 1 and 2 no longer differentiate by location — both may be delivered in
person. The distinction is that tier 1 includes production and presence at the
event; tier 2 is judgement only.

Success is a qualified inbound conversation from a corporate buyer: either a
scoped project inquiry or a speaking/workshop booking.

## Positioning

Information architecture, not presentation design. The claim a neighboring
consultant could not truthfully copy is the method: library science and schema
building applied to executive communication, held over 14 years of global events
rather than assembled per-engagement.

Secondary and non-commercial: AI and IA are treated as one discipline, not two.
The last three months were spent building working products with Claude Code that
people use daily. This is credibility for the core practice, not a service line
being sold — do not present it as an offer.

The Japanese page carries a distinct angle, not a straight translation: it
pitches helping Japanese senior leadership present persuasively to
English-speaking/international clients and investors, and offers an
interpreter for training sessions for those not yet fully confident in
English. English and Portuguese stay on the general positioning above.

## Operating Context

Work happens against a fixed public date that cannot slip. Material arrives late,
incomplete, and from multiple stakeholders who disagree. The deliverable is
consumed once, live, by an audience with no second chance to understand it. Buyers
are frequently a layer removed from the executive who will actually be on stage.

## Capabilities and Constraints

- Delivery across 10+ countries; global events since 2012.
- Founder of Mee (mee.cc), a visual knowledge-management platform. The site lives
  at nepo.mee.cc, a subdomain of that product.
- Site is a static Eleventy build deployed to GitHub Pages on push to `main`.
- Site is available in English, Portuguese, and Japanese (added 2026-08-25),
  one Eleventy template paginated across `/`, `/pt/`, `/ja/`. Language is
  auto-detected from the browser (not IP geolocation — GitHub Pages has no
  server/edge compute), with a manual switcher in the masthead that overrides
  it. See DEPLOYMENT.md's Internationalization section for the mechanics.
- **Undecided:** whether decision-making dashboards and AI/IA product work become
  sellable service lines. Both appear in the About copy as capability and
  credibility. Neither was confirmed as an offer. Do not build page structure that
  presents them as purchasable.

## Brand Commitments

- Name: Rafael Nepô (also "Nepô").
- Title: **Information Architect & Presentation Strategist**. Both halves are
  load-bearing — do not shorten to one on any surface, in any language.
- Company founded 2018; copyright notices run from that year. Practice
  experience on global events predates it, from 2012.
- Accent colour `#FFDC1E`, carried from the previous site.
- Cormorant Garamond for text and display; IBM Plex Mono for data and machine
  strings. Established typography, not open for redesign without a reason.
- Voice: first person, plain, unhedged. Willing to be specific and slightly
  contrarian ("is this knowledge, or does it just sound true?"). Not agency
  register. The About copy is the user's own words and is quoted verbatim on the
  live page — treat it as fixed content, not draft copy.
- Contact is a single address, `contact@mee.cc`. No forms.

## Evidence on Hand

- Since 2012, working with C-suite and senior leadership; 100+ conferences,
  workshops, symposiums and summits; 10+ countries.
- Work delivered for Gartner, NVIDIA and Blizzard — **and others not named**.
  Two standing constraints, both confirmed by the user: keep the softer "work
  delivered for" framing rather than a direct client claim, and signal that the
  three named accounts are a sample rather than the full list. Do not upgrade
  the framing, and do not state a client count.
- Positioning is **premium only**. Surfaces address senior decision-makers; no
  copy that implies volume, entry-level engagements, or price competition.
- Partner at Lilo.Zone (creative studio and maker space, 30+ member community).
- A decade supporting DiaTipo TypeCon, Brazil's largest typography conference.
- Contributor to the Future of Text symposium and book.
- Prior site archived on branch `archive/full-site` and tag `v1-full-site`.
- **Absences that must not be fabricated:** no testimonials, no named case
  studies, no metrics on outcomes, no pricing, no logo assets. There is currently
  no photograph of the user in the repository; the hero runs on a documented CSS
  placeholder awaiting one.

## Product Principles

1. **Structure is the product.** The visible craft is downstream of the schema.
   Anything on a surface that implies decoration-first is off-position.
2. **Specific beats polished.** Concrete numbers, named events, real years. No
   claim that could be lifted onto another consultant's page unchanged.
3. **The buyer is de-risking, not discovering.** Every surface answers "can this
   person be trusted with a moment that cannot be redone."
4. **Never manufacture proof.** The evidence list above is the complete set.
5. **Two ways in, both ungated.** The email address and a four-field inquiry
   form (Formspree, notifications to contact@mee.cc) sit side by side. Superseded
   the earlier "no forms" rule on 2026-08-05 at the user's direction. The spirit
   still holds: nothing is gated, no calendar, no downloads-for-details, no
   multi-step qualification. Adding steps needs a fresh decision.

## Accessibility & Inclusion

No product-specific requirement established. Default target is WCAG AA.
