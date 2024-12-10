import { defineConfig } from 'vite';
import laravel from 'laravel-vite-plugin';
import vue from '@vitejs/plugin-vue';
import { templateCompilerOptions } from '@tresjs/core'
import path from 'path';

export default defineConfig({
    server: {
        host: '0.0.0.0',
        port: 3000,
        hmr: {
            host: "localhost",
        },
        host: true,
    },
    plugins: [
        laravel({
            input: 'resources/js/app.js',
            refresh: true,
        }),
        vue({
            template: {
                transformAssetUrls: {
                    base: null,
                    includeAbsolute: false,
                },
            },
            ...templateCompilerOptions
        }),
    ],
    resolve: {
        alias: {
            '@': path.resolve(__dirname, 'resources/js'),
        }
    }
});
