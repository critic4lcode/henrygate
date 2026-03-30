<script lang="ts">
  import type { TimelineEvent } from '../lib/types.js';
  import EventCard from './EventCard.svelte';
  import {
    Search, Eye, Shield, TriangleAlert, Coins, ScanSearch, DatabaseZap,
    MapPin, FileText, Building2, UserCheck, Clock, Server, Telescope, Circle,
  } from 'lucide-svelte';

  const ICON_MAP: Record<string, unknown> = {
    Search, Eye, Shield, TriangleAlert, Coins, ScanSearch, DatabaseZap,
    MapPin, FileText, Building2, UserCheck, Clock, Server, Telescope, Circle,
  };

  let { events, reversed }: { events: TimelineEvent[]; reversed: boolean } = $props();
  let expanded = $state<string | null>(null);
  let displayEvents = $derived(reversed ? [...events].toReversed() : events);

  function toggle(id: string) {
    expanded = expanded === id ? null : id;
  }
</script>

<div class="relative w-full max-w-[90rem] mx-auto px-4 sm:px-8 lg:px-16 py-16">

  <!-- Mobile: single column with left axis line -->
  <div class="md:hidden">
    <div class="flex flex-col">
      {#each displayEvents as event (event.id)}
        {@const Icon = (ICON_MAP[event.iconName] ?? Circle) as any}
        <div class="flex items-start gap-3">
          <!-- Gutter: line + icon -->
          <div class="relative flex flex-col items-center w-8 flex-none self-stretch">
            <div
              class="absolute top-0 bottom-0 w-px left-1/2 -translate-x-1/2"
              style="background-color: hsl(var(--border));"
            ></div>
            <div
              class="relative mt-4 flex items-center justify-center w-7 h-7 rounded-full z-10 flex-none"
              style="
                background-color: {event.iconBg};
                box-shadow: 0 0 0 2px {event.iconFg}33;
              "
            >
              <Icon size={14} color={event.iconFg} />
            </div>
          </div>
          <!-- Card -->
          <div class="flex-1 min-w-0 pb-8">
            <EventCard
              {event}
              isExpanded={expanded === event.id}
              ontoggle={() => toggle(event.id)}
            />
          </div>
        </div>
      {/each}
    </div>
  </div>

  <!-- Desktop: two-column with center axis -->
  <div class="hidden md:block">
    <!-- Center vertical axis -->
    <div
      class="absolute top-0 bottom-0 w-px"
      style="left: 50%; transform: translateX(-50%); background-color: hsl(var(--border));"
    ></div>

    <div class="flex flex-col gap-12">
      {#each displayEvents as event, i (event.id)}
        {@const Icon = (ICON_MAP[event.iconName] ?? Circle) as any}
        <div class="relative grid grid-cols-2 gap-16 items-start">
          <!-- Left slot -->
          <div class="flex justify-end">
            {#if i % 2 === 0}
              <EventCard
                {event}
                isExpanded={expanded === event.id}
                ontoggle={() => toggle(event.id)}
              />
            {/if}
          </div>

          <!-- Center icon -->
          <div
            class="absolute flex items-center justify-center w-8 h-8 rounded-full"
            style="
              left: 50%;
              top: 1rem;
              transform: translateX(-50%);
              background-color: {event.iconBg};
              box-shadow: 0 0 0 2px {event.iconFg}33;
            "
          >
            <Icon size={15} color={event.iconFg} />
          </div>

          <!-- Right slot -->
          <div class="flex justify-start">
            {#if i % 2 !== 0}
              <EventCard
                {event}
                isExpanded={expanded === event.id}
                ontoggle={() => toggle(event.id)}
              />
            {/if}
          </div>
        </div>
      {/each}
    </div>
  </div>

</div>
