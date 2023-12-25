import { createTamagui, createFont } from 'tamagui';

const myFont = createFont({
  family: 'System',
  weight: {
    4: '400',
    6: '600',
  },
  size: {
    4: 14,
    6: 18,
  },
});

export default createTamagui({
  fonts: {
    myFont,
  },
  themes: {
    light: {
      color: '#000',
      background: '#fff',
    },
    dark: {
      color: '#fff',
      background: '#000',
    },
  },
  shorthands: {},
});