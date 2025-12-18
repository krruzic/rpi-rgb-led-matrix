// -*- mode: c++; c-basic-offset: 2; indent-tabs-mode: nil; -*-
// Minimal graphics utilities - only Color struct for basic pixel operations.
//
// For advanced graphics operations (text, shapes, images), use external
// libraries like PIL/Pillow, Cairo, or other graphics libraries.
#ifndef RPI_GRAPHICS_H
#define RPI_GRAPHICS_H

#include <stdint.h>

namespace rgb_matrix {

struct Color {
  Color() : r(0), g(0), b(0) {}
  Color(uint8_t rr, uint8_t gg, uint8_t bb) : r(rr), g(gg), b(bb) {}
  uint8_t r;
  uint8_t g;
  uint8_t b;
};

}  // namespace rgb_matrix

#endif  // RPI_GRAPHICS_H
