const pkg = require("./package");

module.exports = {
  mode: "spa",
  buildModules: ["@nuxt/typescript-build"],
  server: {
    port: process.env.PORT || 3000,
    host: "localhost"
  },
  output: {
    library: "someLibName",
    libraryTarget: "umd",
    filename: "someLibName.js",
    auxiliaryComment: "Test Comment"
  },
  env: {
    baseUrl: process.env.BASE_URL || "http://localhost:8000",
    websiteUrl: process.env.WEBSITE_URL || "http://localhost:3000",
    route: {
      base: "/management/"
    }
  },
  /*
   ** Headers of the page
   */
  title: "Recruiting analytics platform",
  head: {
    meta: [
      {
        charset: "utf-8"
      },
      {
        name: "viewport",
        content: "width=device-width, initial-scale=1"
      },
      {
        hid: "description",
        name: "description",
        content: pkg.description
      }
    ]
  },

  router: {
    base: "/management/"
  },
  /*
   ** Customize the progress-bar color
   */
  loading: {
    color: "#fff"
  },

  /*
   ** JS
   */
  script: [
    {
      src: "https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"
    }
  ],
  /*
   ** Global CSS
   */
  css: ["~assets/scss/global.scss"],
  styleResources: {
    scss: ["~/assets/scss/*.scss"]
  },
  /*
   ** Plugins to load before mounting the App
   */
  plugins: [
    {
      src: "~/plugins/OwnAxios"
    },
  ],
  /*
   ** Nuxt.js modules
   */
  modules: [
    // Doc: https://bootstrap-vue.js.org/docs/
    "bootstrap-vue/nuxt",
    [
      "nuxt-fontawesome",
      {
        imports: [
          {
            set: "@fortawesome/free-solid-svg-icons",
            icons: ["fas"]
          },
          {
            set: "@fortawesome/free-brands-svg-icons",
            icons: ["fab"]
          },
          {
            set: "@fortawesome/free-regular-svg-icons",
            icons: ["far"]
          }
        ]
      }
    ],
    [
      "nuxt-mq",
      {
        // Default breakpoint for SSR
        defaultBreakpoint: "default",
        breakpoints: {
          mobile: 450,
          tablet: 900,
          desktop: 1250
        }
      }
    ],
    [
      "@nuxtjs/axios",
      {
        baseURL: process.env.BASE_URL || "http://localhost:8000"
      }
    ],
    "nuxt-lazy-load"
  ],
  /*
   ** Build configuration
   */
  build: {
    /*
     ** You can extend webpack config here
     */

    splitChunks: {
      layouts: true,
      pages: true
    },
    plugins: [],
    extend(config, ctx) {
      if (ctx.isDev) {
        // https://medium.com/js-dojo/debugging-nuxt-js-with-vs-code-60a1a9e75cf6
        config.devtool = ctx.isClient ? "source-map" : "inline-source-map";
      } else {
        config.devtool = "hidden-source-map";
      }

      const svgRule = config.module.rules.find(rule => rule.test.test(".svg"));

      svgRule.test = /\.(png|jpe?g|gif|webp)$/;

      config.module.rules.push({
        test: /\.svg$/,
        use: ["babel-loader", "vue-svg-loader"]
      });
    }
  }
};
