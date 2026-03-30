import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';
import tailwindcss from '@tailwindcss/vite';
import matter from 'gray-matter';
import { marked } from 'marked';

// Parses .md files into JS modules at build time (Node context).
// This keeps gray-matter and marked out of the browser bundle entirely.
function markdownPlugin() {
  return {
    name: 'markdown-transform',
    transform(code: string, id: string) {
      if (!id.endsWith('.md')) return null;
      const { data, content } = matter(code);
      const bodyHtml = marked(content) as string;
      return {
        code: `export default ${JSON.stringify({ data, bodyHtml })}`,
        map: null,
      };
    },
  };
}

export default defineConfig({
  base: process.env.NODE_ENV === 'production' ? '/henrygate/' : '/',
  plugins: [
    tailwindcss(),
    markdownPlugin(),
    svelte(),
  ],
  build: {
    outDir: 'docs',
    emptyOutDir: false,
    rollupOptions: {
      output: {
        entryFileNames: 'assets/index.js',
        chunkFileNames: 'assets/index.js',
        assetFileNames: 'assets/index.[ext]',
      },
    },
  },
});
