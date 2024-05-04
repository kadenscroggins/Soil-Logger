in = 25.4; // Conv. to inches

board_width = 2 * in;
board_depth = 0.9 * in;
hole_rad = 0.05 * in;
hole_dist_edge = 0.1 * in;
hole_sep_depth = 0.7 * in;
hole_sep_width = 1.8 * in;

shell_thickness = 0.1 * in;
shell_gap = 0.01 * in;
peg_len = 0.8 * in;
peg_gap = 0.01 * in;

module peg(x,y,z) {
    translate([x,y,z]) {
        cylinder(
            h = peg_len,
            r = hole_rad - peg_gap,
            $fn = 90
        );
    }
}

union() {
    cube([
        board_width + shell_gap,
        board_depth + shell_gap,
        shell_thickness
    ]);

    peg(
        hole_dist_edge,
        hole_dist_edge,
        0
    );

    peg(
        hole_dist_edge,
        hole_dist_edge + hole_sep_depth,
        0
    );

    peg(
        hole_dist_edge + hole_sep_width,
        hole_dist_edge,
        0
    );

    peg(
        hole_dist_edge + hole_sep_width,
        hole_dist_edge + hole_sep_depth,
        0
    );
}
