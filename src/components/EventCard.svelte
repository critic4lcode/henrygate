<script lang="ts">
  import type { TimelineEvent } from '../lib/types.js';
  import EventDetail from './EventDetail.svelte';
  import { cn } from '../lib/utils.js';

  let {
    event,
    isExpanded,
    ontoggle,
  }: {
    event: TimelineEvent;
    isExpanded: boolean;
    ontoggle: () => void;
  } = $props();
</script>

<div
  class={cn(
    'w-full rounded-lg shadow-sm transition-all duration-200',
    'border',
  )}
  style="
    background-color: hsl(var(--card));
    color: hsl(var(--card-foreground));
    border-color: {isExpanded ? event.accent : 'hsl(var(--border))'};
    box-shadow: {isExpanded ? `0 0 0 1px ${event.accent}` : ''};
  "
>
  <!-- Collapsed header — always visible -->
  <button
    class="w-full text-left p-4 cursor-pointer"
    onclick={ontoggle}
    aria-expanded={isExpanded}
  >
    <time class="text-xs font-mono" style="color: hsl(var(--muted-foreground));">
      {event.dateDisplay}
    </time>
    <h2 class="mt-1 text-sm font-semibold leading-tight">{event.title}</h2>
    {#if event.tags.length}
      <div class="mt-2 flex flex-wrap gap-1">
        {#each event.tags as tag (tag)}
          <span
            class="text-xs px-1.5 py-0.5 rounded"
            style="background-color: hsl(var(--muted)); color: hsl(var(--muted-foreground));"
          >
            {tag}
          </span>
        {/each}
      </div>
    {/if}
  </button>

  <!-- Expanded detail -->
  {#if isExpanded}
    <EventDetail bodyHtml={event.bodyHtml} />
  {/if}
</div>
