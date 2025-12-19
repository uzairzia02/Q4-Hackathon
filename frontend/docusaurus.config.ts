import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'Physical AI and Humanoid Robotics',
  tagline: 'A comprehensive course on building intelligent robots.',
  favicon: 'img/robot-icon.png', // Updated to a robot-themed favicon

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // Set the production url of your site here
  url: process.env.URL || 'https://uzairzia02.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  customFields: {
    backendUrl: process.env.BACKEND_URL || 'http://localhost:8000',
    apiKey: 'OwR0MgBu6o47fBUXA1PX379Up0iONX2004n5EMzo',
  },

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'uzairzia02', // Usually your GitHub org/user name.
  projectName: 'Q4-Hackathon', // Usually your repo name.

  onBrokenLinks: 'throw',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'ur'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/uzairzia02/Q4-Hackathon/tree/main/',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/robot-social-card.jpg', // Updated to a robot-themed social card
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: '🤖 Physical AI & Robotics',
      logo: {
        alt: 'Physical AI and Humanoid Robotics Logo',
        src: 'img/robot-logo.svg', // Updated to a robot-themed logo
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'courseSidebar',
          position: 'left',
          label: '📚 Course',
        },
        {
          to: '/',
          label: 'Home',
          position: 'left'
        },
        {
          href: 'https://github.com/uzairzia02/Q4-Hackathon',
          label: '🐙 GitHub',
          position: 'right',
        },
        {
          href: 'https://www.youtube.com/', // Placeholder for robotics-related video
          label: '🎥 Demo',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: '📖 Course Content',
          items: [
            {
              label: 'Introduction',
              to: '/docs/intro',
            },
            {
              label: 'ROS 2 Basics',
              to: '/docs/ros-basics',
            },
            {
              label: 'NVIDIA Isaac',
              to: '/docs/nvidia-isaac',
            },
            {
              label: 'VLA Pipelines',
              to: '/docs/vla-pipelines',
            },
          ],
        },
        {
          title: '🤖 Robotics Resources',
          items: [
            {
              label: 'Gazebo Simulations',
              href: 'https://gazebosim.org/',
            },
            {
              label: 'ROS Documentation',
              href: 'https://docs.ros.org/',
            },
            {
              label: 'NVIDIA Isaac Docs',
              href: 'https://docs.nvidia.com/isaac/',
            },
          ],
        },
        {
          title: '🔗 Connect',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/uzairzia02/Q4-Hackathon',
            },
            {
              label: 'Discord',
              href: 'https://discordapp.com/invite/robotics',
            },
            {
              label: 'Research Papers',
              href: 'https://arxiv.org/list/cs.RO/recent',
            },
          ],
        },
      ],
      copyright: `🤖 Copyright © ${new Date().getFullYear()} Physical AI and Humanoid Robotics Course. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.oneDark, // Changed to a more tech-themed theme
      darkTheme: prismThemes.oneDark,
      additionalLanguages: ['python', 'bash', 'json', 'yaml', 'docker'],
    },
    // algolia: {
    //   // The application ID provided by Algolia
    //   appId: 'YOUR_ALGOLIA_APP_ID',
    //   // Public API key: it is safe to commit it
    //   apiKey: 'YOUR_ALGOLIA_API_KEY',
    //   indexName: 'your-index-name',
    //   contextualSearch: true,
    // },
  } satisfies Preset.ThemeConfig,
};

export default config;
