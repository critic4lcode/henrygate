<script lang="ts">
  let { bodyHtml }: { bodyHtml: string } = $props();
</script>

<div class="border-t p-4" style="border-color: hsl(var(--border));">
  <div class="prose prose-sm max-w-none dark:prose-invert">
    {@html bodyHtml}
  </div>
</div>
