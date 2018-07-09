<template>
<svg style="width: 100%; height: 100%">
  <g>
    <g></g>
    <g>
    <template v-for="s in layout">
      <template v-if="s.rect">
      <g style="visibility: visible;" transform="translate(0.5, 0.5)">
        <path :d="s.arrow_line" fill="none" stroke="white" stroke-miterlimit="10" pointer-events="stroke" visibility="hidden" stroke-width="9"></path>
        <path :d="s.arrow_line" fill="none" stroke="#666666" stroke-miterlimit="10"></path>
        <path :d="s.arrow_head" fill="#666666" stroke="#666666" stroke-miterlimit="10" pointer-events="all"></path>
      </g>
      <g style="visibility: visible; cursor: pointer;" transform="translate(0.5,0.5)">
        <rect :x="s.rect[0]" :y=" s.rect[1]" :width=" s.rect[2] " :height=" s.rect[3] " :fill="s.fill" :stroke="s.stroke" pointer-events="all"></rect>
      </g>
      <g style="cursor: pointer;">
        <g :transform="s.translate">
          <foreignObject style="overflow:visible;" pointer-events="all" width="29" height="12">
            <div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; vertical-align: top; width: 30px; white-space: normal; overflow-wrap: normal; text-decoration: underline; text-align: center;">
              <div xmlns="http://www.w3.org/1999/xhtml" style="display:inline-block;text-align:inherit;text-decoration:inherit;">{{ s.name }}
              </div>
            </div>
          </foreignObject>
        </g>
      </g>
      </template>
      <template v-else>
      <g style="visibility: visible;" transform="translate(0.5,0.5)">
        <ellipse :cx="s.ellipse[0]" :cy="s.ellipse[1]" :rx="s.ellipse[2]" :ry="s.ellipse[3]" :fill="s.fill" :stroke="s.stroke" pointer-events="all">
        </ellipse>
      </g>
      <g style="">
        <g :transform="s.translate">
          <foreignObject style="overflow:visible;" pointer-events="all" width="33" height="12">
            <div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; vertical-align: top; width: 34px; white-space: normal; overflow-wrap: normal; text-align: center;">
              <div xmlns="http://www.w3.org/1999/xhtml" style="display:inline-block;text-align:inherit;text-decoration:inherit;">{{ s.name }}
              </div>
            </div>
          </foreignObject>
        </g>
      </g>
      </template>
      </template>
    </g>
  </g>
</svg>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
      msg: 'Welcome to Beam Commissioning App',
      layout: [
        { 'name': 'LEBT',
          'arrow': true,
          'arrow_line': 'M 87 165 L 99.74 165',
          'arrow_head': 'M 104.9 165 L 98.01 168.44 L 99.74 165 L 98.01 161.56 Z',
          'rect': [7.87, 145.61, 78.71, 39.35],
          'translate': 'translate(32, 159)scale(0.9838249286393911)',
          'fill': '#ffe6cc',
          'stroke': '#d79b00',
        },
        { 'name': 'RFQ',
          'arrow': true,
          'arrow_line': 'M 185 165 L 198.74 165',
          'arrow_head': 'M 203.9 165 L 197.01 168.44 L 198.74 165 L 197.01 161.56 Z',
          'rect': [106.25, 145.61, 78.71, 39.35],
          'translate': 'translate(130, 159)scale(0.9838249286393911)',
          'fill': '#ffe6cc',
          'stroke': '#d79b00',
        },
        { 'name': 'MEBT',
          'arrow': true,
          'arrow_line': 'M 283 165 L 296.74 165',
          'arrow_head': 'M 301.9 165 L 295.01 168.44 L 296.74 165 L 295.01 161.56 Z',
          'rect': [204.64, 145.61, 78.71, 39.35],
          'translate': 'translate(231, 159)scale(0.9838249286393911)',
          'fill': '#ffe6cc',
          'stroke': '#d79b00',
        },
        { 'name': 'CM1',
          'arrow': true,
          'arrow_line': 'M 382 165 L 394.74 165',
          'arrow_head': 'M 399.9 165 L 393.01 168.44 L 394.74 165 L 393.01 161.56 Z',
          'rect': [303.02, 145.61, 78.71, 39.35],
          'translate': 'translate(326, 159)scale(0.9838249286393911)',
          'fill': '#e1d5e7',
          'stroke': '#9673a6',
        },
        { 'name': 'CM2',
          'arrow': true,
          'arrow_line': 'M 480 165 L 493.74 165',
          'arrow_head': 'M 498.9 165 L 492.01 168.44 L 494.74 165 L 492.01 161.56 Z',
          'rect': [401.4, 145.61, 78.71, 39.35],
          'translate': 'translate(429, 159)scale(0.9838249286393911)',
          'fill': '#e1d5e7',
          'stroke': '#9673a6',
        },
        { 'name': 'CM3',
          'arrow': true,
          'arrow_line': 'M 578 165 L 591.74 165',
          'arrow_head': 'M 596.9 165 L 590.01 168.44 L 591.74 165 L 590.01 161.56 Z',
          'rect': [499.78, 145.61, 78.71, 39.35],
          'translate': 'translate(527, 159)scale(0.9838249286393911)',
          'fill': '#e1d5e7',
          'stroke': '#9673a6',
        },
        { 'name': 'CM4',
          'arrow': true,
          'arrow_line': 'M 677 165 L 690.74 165',
          'arrow_head': 'M 695.9 165 L 689.01 168.44 L 690.74 165 L 689.01 161.56 Z',
          'rect': [598.17, 145.61, 78.71, 39.35],
          'translate': 'translate(625, 159)scale(0.9838249286393911)',
          'fill': '#e1d5e7',
          'stroke': '#9673a6',
        },
        { 'name': 'HEBT',
          'arrow': true,
          'arrow_line': 'M 775 165 L 788.74 165',
          'arrow_head': 'M 793.9 165 L 787.01 168.44 L 788.74 165 L 787.01 161.56 Z',
          'rect': [696.55, 145.61, 78.71, 39.35],
          'translate': 'translate(724, 159)scale(0.9838249286393911)',
          'fill': '#f8cecc',
          'stroke': '#b85450',
        },
        { 'name': 'Dump',
          'arrow': false,
          'ellipse': [814, 165, 19.6765, 19.6765],
          'translate': 'translate(797, 159)scale(0.9838249286393911)',
          'fill': '#f8cecc',
          'stroke': '#b85450',
        },
      ]
    }
  }
}
</script>

</style>
