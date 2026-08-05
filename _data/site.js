module.exports = {
  name: "Rafael Nepô",
  title: "Rafael Nepô — Information Architect & Presentation Strategist",
  description: "Conference and event architecture, and the narratives senior leaders take on stage with it — for material that gets one chance to land.",
  url: "https://nepo.mee.cc",
  email: "contact@mee.cc",
  entity: "mee.cc",
  // Formspree endpoint. While empty the page falls back to the plain
  // mailto:, so a missing value can never ship a form that posts nowhere.
  formEndpoint: "https://formspree.io/f/mkjwnbrz",
  location: "Brazil · US · Japan",
  // Flags shown beside the countries claim, in the one-pager's order.
  // The line still reads "10+" — these are the ones with illustrations,
  // not the full count, so naming nine never contradicts the number.
  // Assets: Irasutoya, trimmed and resized by hand into images/flags/.
  countries: [
    { code: "br", name: "Brazil" },
    { code: "jp", name: "Japan" },
    { code: "us", name: "United States" },
    { code: "in", name: "India" },
    { code: "mx", name: "Mexico" },
    { code: "au", name: "Australia" }
  ],
  author: "Rafael Nepô",
  founded: 2018,
  year: new Date().getFullYear(),
  // Two-digit end of the copyright span — "2018–26" rather than
  // "2018–2026", which wrapped the colophon onto a second line on phones.
  yearShort: String(new Date().getFullYear()).slice(-2)
};
