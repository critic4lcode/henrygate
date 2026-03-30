export interface EventTheme {
  iconName: string;
  iconBg: string;
  iconFg: string;
  accent: string;
}

const MAPPINGS: Array<{ tags: string[]; theme: EventTheme }> = [
  // Házkutatás — razzia (scan-search = keresés otthon)
  {
    tags: ['házkutatás'],
    theme: { iconName: 'ScanSearch', iconBg: '#fee2e2', iconFg: '#b91c1c', accent: '#ef4444' },
  },
  // Gyanúsítás / vád
  {
    tags: ['gyanusitas', 'haditechnikai'],
    theme: { iconName: 'TriangleAlert', iconBg: '#fef9c3', iconFg: '#ca8a04', accent: '#eab308' },
  },
  // Megfigyelés / kémkedés / operatív (távcső = surveillance)
  {
    tags: ['titkosszolgálat', 'henry', 'mos4ik', 'mosaic'],
    theme: { iconName: 'Telescope', iconBg: '#fce7f3', iconFg: '#be185d', accent: '#ec4899' },
  },
  // Toborzás / befolyásolás
  {
    tags: ['beszervezés'],
    theme: { iconName: 'UserCheck', iconBg: '#fff7ed', iconFg: '#c2410c', accent: '#f97316' },
  },
  // Nyomozás (nagyító)
  {
    tags: ['nni', 'arnyeknyomozas', 'szabo-bence'],
    theme: { iconName: 'Search', iconBg: '#ede9fe', iconFg: '#7c3aed', accent: '#8b5cf6' },
  },
  // Adatszivárgás
  {
    tags: ['adatszivárgás', 'visszhang', 'tiszavilag'],
    theme: { iconName: 'DatabaseZap', iconBg: '#ffedd5', iconFg: '#ea580c', accent: '#f97316' },
  },
  // Pénz / kripto
  {
    tags: ['monero', 'hackeles'],
    theme: { iconName: 'Coins', iconBg: '#fef3c7', iconFg: '#d97706', accent: '#f59e0b' },
  },
  // Találkozó / utazás
  {
    tags: ['találkozó', 'kijev', 'ukrajna', 'önkéntes'],
    theme: { iconName: 'MapPin', iconBg: '#ccfbf1', iconFg: '#0f766e', accent: '#14b8a6' },
  },
  // Kiberbiztonság / NATO
  {
    tags: ['kiberbiztonság', 'kibervédelem', 'nato', 'ccdcoe'],
    theme: { iconName: 'Shield', iconBg: '#dbeafe', iconFg: '#2563eb', accent: '#3b82f6' },
  },
  // Nyilatkozat / sajtó / bejelentés
  {
    tags: ['nyilatkozat', 'direkt36', 'bejelentés', 'nmhh'],
    theme: { iconName: 'FileText', iconBg: '#f1f5f9', iconFg: '#475569', accent: '#64748b' },
  },
  // Szervezet / hatóság
  {
    tags: ['stohastik', 'brit', 'hajó', 'ah', 'nbsz', 'ov'],
    theme: { iconName: 'Building2', iconBg: '#e0e7ff', iconFg: '#4338ca', accent: '#6366f1' },
  },
  // IT infrastruktúra
  {
    tags: ['infrastruktúra', 'it'],
    theme: { iconName: 'Server', iconBg: '#eff6ff', iconFg: '#1d4ed8', accent: '#3b82f6' },
  },
  // Előzmény / háttér
  {
    tags: ['előzmény'],
    theme: { iconName: 'Clock', iconBg: '#f3f4f6', iconFg: '#6b7280', accent: '#9ca3af' },
  },
];

const DEFAULT_THEME: EventTheme = {
  iconName: 'Circle',
  iconBg: 'hsl(var(--primary) / 0.15)',
  iconFg: 'hsl(var(--primary))',
  accent: 'hsl(var(--primary))',
};

export function getEventTheme(tags: string[]): EventTheme {
  const lower = tags.map((t) => t.toLowerCase());
  for (const { tags: triggers, theme } of MAPPINGS) {
    if (triggers.some((t) => lower.includes(t))) return theme;
  }
  return DEFAULT_THEME;
}
