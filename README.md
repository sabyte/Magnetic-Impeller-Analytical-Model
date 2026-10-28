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

## Assumptions and limits

- The magnet is the K&J D48DIA in grade N42, as confirmed by the person who ran the experiments. The side panel lets you change Br to test other values.
- Distances are center-to-center, measured from the magnet's axis to the sensor, with the shaft parallel to the sensor's X axis.
- Quasi-static field (no eddy currents), no steel or other magnetic material near the magnet, uniform magnetization.
- Section 6 of the page (pump physics) uses example impeller dimensions. Replace them with the real ones.
- The first 20 mm attempt was misaligned and is shown only as a grey marker. It is not in `data/`.

## Files

- `index.html`: the interactive page. One file, no build step. It loads the fonts from Google Fonts and works without them.
- `data/measured_summary.csv`: per-distance results (mean of per-revolution ellipse fits).
- `analysis/field_model.py`: finite-cylinder field by numerical integration (needs numpy).
- `analysis/predict.py`: reproduces the table above. Run `python3 predict.py` inside `analysis/`.

## Publish on GitHub Pages

1. Create a repository and upload the contents of this folder to the top level (not the folder itself).
2. Settings → Pages → Deploy from a branch → `main` → `/ (root)` → Save.
3. The site appears at `https://YOUR-USERNAME.github.io/REPOSITORY-NAME/`.

GitHub Pages sites are public, even when the repository is private.
