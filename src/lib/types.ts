export interface HomeConfig {
  title: string;
  subtitle: string;
  sourcesHtml: string;
  contributeUrl?: string;
}

export interface TimelineEvent {
  id: string;
  date: string;
  dateDisplay: string;
  title: string;
  tags: string[];
  bodyHtml: string;
  side: 'left' | 'right';
  iconName: string;
  iconBg: string;
  iconFg: string;
  accent: string;
}
