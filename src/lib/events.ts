import type { TimelineEvent, HomeConfig } from './types.js';
import { getEventTheme } from './eventIcon.js';

interface MarkdownModule {
  default: {
    data: { date?: unknown; title?: unknown; tags?: unknown };
    bodyHtml: string;
  };
}

// .md files are transformed to JS by markdownPlugin in vite.config.ts.
// No gray-matter or marked in the browser — only plain data.
const modules = import.meta.glob('/content/*.md', { eager: true }) as Record<string, MarkdownModule>;

const HU_MONTHS = [
  'január', 'február', 'március', 'április', 'május', 'június',
  'július', 'augusztus', 'szeptember', 'október', 'november', 'december',
];

function formatDateDisplay(raw: string): string {
  const [year, month, day] = raw.split('-');
  const yearKnown = year && !year.includes('?');
  const monthKnown = month && !month.includes('?');
  const dayKnown = day && !day.includes('?');

  if (!yearKnown) return 'ismeretlen dátum';
  if (!monthKnown) return `${year} körül`;
  const monthName = HU_MONTHS[parseInt(month, 10) - 1] ?? month;
  if (!dayKnown) return `${year}. ${monthName} körül`;
  return `${year}. ${monthName} ${parseInt(day, 10)}.`;
}

function sortKey(raw: string): string {
  return raw.replace(/\?/g, '0');
}

export function loadHomeConfig(): HomeConfig {
  const entry = Object.entries(modules).find(([path]) =>
    path.endsWith('/0000-home.md')
  );
  if (!entry) return { title: 'Timeline', subtitle: '', sourcesHtml: '' };
  const { data, bodyHtml } = entry[1].default;
  return {
    title: String(data.title ?? 'Timeline'),
    subtitle: String(data.subtitle ?? ''),
    sourcesHtml: bodyHtml,
    contributeUrl: data.contribute_url ? String(data.contribute_url) : undefined,
  };
}

export function loadEvents(): TimelineEvent[] {
  const events = Object.entries(modules)
    .filter(([path]) => !path.endsWith('/0000-home.md'))
    .map(([path, mod]) => {
    const { data, bodyHtml } = mod.default;
    const id = path.split('/').pop()!.replace(/\.md$/, '');
    const tags = Array.isArray(data.tags) ? (data.tags as string[]) : [];
    const theme = getEventTheme(tags);
    const date = String(data.date ?? '');
    return {
      id,
      date,
      dateDisplay: formatDateDisplay(date),
      title: String(data.title ?? id),
      tags,
      bodyHtml,
      side: 'left' as const,
      ...theme,
    };
  });

  events.sort((a, b) => sortKey(a.date).localeCompare(sortKey(b.date)));
  events.forEach((e, i) => {
    e.side = i % 2 === 0 ? 'left' : 'right';
  });

  return events;
}
