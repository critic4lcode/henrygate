<script lang="ts">
  import { Moon, Sun } from 'lucide-svelte';

  let dark = $state(false);

  $effect(() => {
    const stored = localStorage.getItem('theme');
    if (stored === 'dark' || (!stored && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
      dark = true;
    }
  });

  $effect(() => {
    document.documentElement.classList.toggle('dark', dark);
    localStorage.setItem('theme', dark ? 'dark' : 'light');
  });
</script>

<button
  onclick={() => dark = !dark}
  class="flex items-center justify-center w-8 h-8 rounded-md border transition-colors"
  style="border-color: hsl(var(--border)); color: hsl(var(--muted-foreground));"
  aria-label={dark ? 'Váltás világos módra' : 'Váltás sötét módra'}
>
  {#if dark}
    <Sun size={15} />
  {:else}
    <Moon size={15} />
  {/if}
</button>
