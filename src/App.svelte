<script lang="ts">
  import { loadEvents, loadHomeConfig } from './lib/events.js';
  import Timeline from './components/Timeline.svelte';
  import ThemeToggle from './components/ThemeToggle.svelte';

  const events = loadEvents();
  const home = loadHomeConfig();
  let reversed = $state(false);
</script>

<main class="min-h-screen" style="background-color: hsl(var(--background)); color: hsl(var(--foreground));">
  <header class="py-10 text-center" style="border-bottom: 1px solid hsl(var(--border));">
    <div class="relative">
      <h1 class="text-4xl font-bold tracking-tight">{home.title}</h1>
      <div class="hidden sm:flex absolute right-4 top-1/2 -translate-y-1/2 items-center gap-2">
        <button
          onclick={() => reversed = !reversed}
          class="flex items-center gap-1.5 text-sm px-3 py-1.5 rounded-md border transition-colors"
          style="border-color: hsl(var(--border)); color: hsl(var(--muted-foreground));"
        >
          {#if reversed}
            <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5"/><path d="m5 12 7-7 7 7"/></svg>
            Újabb → Régebbi
          {:else}
            <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14"/><path d="m19 12-7 7-7-7"/></svg>
            Régebbi → Újabb
          {/if}
        </button>
        <ThemeToggle />
      </div>
    </div>
    {#if home.subtitle}
      <p class="mt-2 text-sm max-w-2xl mx-auto px-4" style="color: hsl(var(--muted-foreground));">{home.subtitle}</p>
    {/if}
    {#if home.contributeUrl}
      <div class="mt-4 inline-flex flex-wrap justify-center items-center gap-2">
        <span class="text-xs" style="color: hsl(var(--muted-foreground));">Új információd van?</span>
        <a
          href="{home.contributeUrl}/issues/new"
          target="_blank"
          rel="noopener noreferrer"
          class="inline-flex items-center gap-1.5 text-xs px-3 py-1.5 rounded-md border transition-colors"
          style="border-color: hsl(var(--border)); color: hsl(var(--muted-foreground)); background-color: hsl(var(--card));"
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
          Issue létrehozása
        </a>
        <a
          href="{home.contributeUrl}/pulls"
          target="_blank"
          rel="noopener noreferrer"
          class="inline-flex items-center gap-1.5 text-xs px-3 py-1.5 rounded-md border transition-colors"
          style="border-color: hsl(var(--border)); color: hsl(var(--muted-foreground)); background-color: hsl(var(--card));"
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="18" r="3"/><circle cx="6" cy="6" r="3"/><path d="M13 6h3a2 2 0 0 1 2 2v7"/><line x1="6" y1="9" x2="6" y2="21"/></svg>
          Pull request
        </a>
      </div>
    {/if}
    <div class="flex sm:hidden justify-center items-center gap-2 mt-4">
      <button
        onclick={() => reversed = !reversed}
        class="flex items-center gap-1.5 text-sm px-3 py-1.5 rounded-md border transition-colors"
        style="border-color: hsl(var(--border)); color: hsl(var(--muted-foreground));"
      >
        {#if reversed}
          <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5"/><path d="m5 12 7-7 7 7"/></svg>
          Újabb → Régebbi
        {:else}
          <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14"/><path d="m19 12-7 7-7-7"/></svg>
          Régebbi → Újabb
        {/if}
      </button>
      <ThemeToggle />
    </div>
  </header>
  <Timeline {events} {reversed} />

  {#if home.sourcesHtml}
    <footer class="w-full max-w-[90rem] mx-auto px-4 sm:px-8 lg:px-16 pb-16 pt-4" style="border-top: 1px solid hsl(var(--border));">
      {#if home.sourcesHtml}
        <div class="prose prose-sm max-w-none dark:prose-invert" style="color: hsl(var(--muted-foreground));">
          {@html home.sourcesHtml}
        </div>
      {/if}
    </footer>
  {/if}
</main>
