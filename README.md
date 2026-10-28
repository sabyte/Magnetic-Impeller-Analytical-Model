# Rotating field of an N20-driven diametric magnet: analytical model

An interactive page (`index.html`) that predicts the field a spinning diametric NdFeB magnet produces at a TLE493D-W2B6 Hall sensor, and compares the prediction with measurements at 12, 20, 30 and 37 mm (12 V, about 570 revolutions each).

## What is modelled

- Magnet: K&J D48DIA, 6.35 mm diameter × 12.70 mm long, grade N42, Br = 13,200 G (1.32 T), diametrically magnetized ([datasheet page](http://www.kjmagnetics.com/d48dia-neodymium-diametric-cylinder-magnet?cat=8)). The size matches the caliper measurement on the actual magnet (length 12.73 mm).
- Physics: a uniformly magnetized cylinder is equivalent to a surface "magnetic charge" σ = M·n on its curved side. Far away this is a point dipole m = (Br/μ0)·V, giving a radial field twice the tangential one, both ∝ r⁻³. Rotating the magnet traces an ellipse. The finite-size version integrates the surface charge over the cylinder.
- The strength is taken from the datasheet. **Nothing is fitted to the measurements** unless you choose a calibration distance in the side panel.

## Result

| Distance | Radial Br: predicted / measured (mT) | Error | Tangential Bt: predicted / measured (mT) | Error |
|---|---|---|---|---|
| 12 mm | 39.5 / 46.6 | −15% | 22.0 / 25.5 | −14% |
| 20 mm | 9.75 / 9.31 | +4.7% | 5.07 / 4.57 | +11% |
| 30 mm | 3.02 / 2.98 | +1.4% | 1.54 / 1.33 | +15% |
| 37 mm | 1.63 / 1.58 | +2.8% | 0.82 / 0.67 | +23% |

Three of four radial predictions are within 5%. The page discusses the remaining gaps (placement sensitivity at 12 mm, magnet tolerances, the tangential trend and sensor resolution) and a test for each.

## Flow validation (dye front, 50% impeller)

Nine runs at 12, 20 and 30 mm and 8, 10 and 12 V (34.2, 43.3 and 53.77 Hz), with the dye front timed over 4.0 cm (`data/dye_flow.csv`). Impeller: Ø5 × 10 mm three-helix screw, 9 mm pitch (18 mm at full size), in a 6 mm tube, with two K&J B111 cubes (1.59 mm, N42).

- The dye moves 0.81–1.40 mm per turn, 13–22% of the 6.25 mm a leak-free locked screw would give.
- A locked screw with one efficiency predicts flow ∝ f and independent of distance. The data contradict both (18.5% mean error when each distance is predicted from the other two).
- The efficiency collapses onto η = 0.147 Λ^−0.26 (R² = 0.89; frequency alone gives 0.25), where Λ = ω/ω_n = 2πf √(I / (m_i B_t(d))) and B_t(d) comes from the validated field model. Predicting each distance from the other two gives a mean error of 8.6% (worst −17%).
- The rotor inertia is estimated (0.12 g; it rescales Λ but does not change the fit). The next measurement is the impeller's rotation rate from the 0.25× video, which decides whether the coupling stays locked.

## Assumptions and limits

- The magnet is the K&J D48DIA in grade N42, as confirmed by the person who ran the experiments. The side panel lets you change Br to test other values.
- Distances are center-to-center, measured from the magnet's axis to the sensor, with the shaft parallel to the sensor's X axis.
- Quasi-static field (no eddy currents), no steel or other magnetic material near the magnet, uniform magnetization.
- The impeller's rotor mass (0.12 g) is an estimate. All other impeller dimensions are measured values for the 50% model.

## Files

- `index.html`: the interactive page, including the animated Figure 1 (side view, end view and live field trace, all computed from the model). One file, no build step. It loads the fonts from Google Fonts and works without them.
- `data/measured_summary.csv`: per-distance field results (mean of per-revolution ellipse fits).
- `data/dye_flow.csv`: the nine dye-front runs.
- `analysis/field_model.py`: finite-cylinder field by numerical integration (needs numpy).
- `analysis/predict.py`: reproduces the table above. Run `python3 predict.py` inside `analysis/`.

## Publish on GitHub Pages

1. Create a repository and upload the contents of this folder to the top level (not the folder itself).
2. Settings → Pages → Deploy from a branch → `main` → `/ (root)` → Save.
3. The site appears at `https://YOUR-USERNAME.github.io/REPOSITORY-NAME/`.

GitHub Pages sites are public, even when the repository is private.
