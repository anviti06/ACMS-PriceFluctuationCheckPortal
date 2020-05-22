/**
 * Welcome to your Workbox-powered service worker!
 *
 * You'll need to register this file in your web app and you should
 * disable HTTP caching for this file too.
 * See https://goo.gl/nhQhGp
 *
 * The rest of the code is auto-generated. Please don't update this file
 * directly; instead, make changes to your Workbox build configuration
 * and re-run your build process.
 * See https://goo.gl/2aRDsh
 */

importScripts("https://storage.googleapis.com/workbox-cdn/releases/4.3.1/workbox-sw.js");

importScripts(
<<<<<<< HEAD
<<<<<<< HEAD
  "/static/react/precache-manifest.1aa93c1c856c9fc6f5fbe9f2103fd2ee.js"
=======
  "/static/react/precache-manifest.d9efc6ccfedb352843a0e3fc964c12ab.js"
>>>>>>> fae0b194976565a3eac79ffe910bdeccfcc23460
=======
  "/static/react/precache-manifest.b4b3fa15c6cc77657127be18232412e3.js"
>>>>>>> parent of fae0b19... images displayed
);

self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});

workbox.core.clientsClaim();

/**
 * The workboxSW.precacheAndRoute() method efficiently caches and responds to
 * requests for URLs in the manifest.
 * See https://goo.gl/S9QRab
 */
self.__precacheManifest = [].concat(self.__precacheManifest || []);
workbox.precaching.precacheAndRoute(self.__precacheManifest, {});

workbox.routing.registerNavigationRoute(workbox.precaching.getCacheKeyForURL("/static/react/index.html"), {
  
  blacklist: [/^\/_/,/\/[^\/?]+\.[^\/]+$/],
});
