import React from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import { useLocation } from '@docusaurus/router';
import Link from '@docusaurus/Link';
import clsx from 'clsx';
import styles from './LanguageToggle.module.css';

const LanguageToggle: React.FC = () => {
  const {i18n} = useDocusaurusContext();
  const {pathname} = useLocation();
  const {currentLocale, localeConfigs} = i18n;

  // Function to get the path for a specific locale
  const getLocalizedPath = (locale: string) => {
    if (locale === i18n.defaultLocale) {
      // For default locale, remove locale prefix if it exists
      return pathname.replace(`/${currentLocale}`, '');
    } else {
      // For other locales, add the locale prefix
      return `/${locale}${pathname}`;
    }
  };

  if (i18n.locales.length <= 1) {
    return null; // Don't show toggle if only one locale is configured
  }

  return (
    <div className={styles.languageToggle}>
      {i18n.locales.map((locale) => (
        <Link
          key={locale}
          to={getLocalizedPath(locale)}
          className={clsx(styles.toggleButton, {
            [styles.active]: currentLocale === locale,
          })}
          title={localeConfigs[locale].label}
          aria-label={localeConfigs[locale].label}
        >
          {locale.toUpperCase()}
        </Link>
      ))}
    </div>
  );
};

export default LanguageToggle;
