# nusprint — nuScenes BEV detection + light forecasting (scaffold)

## Quickstart
```bash
make up          # build CUDA/PyTorch/nuscenes-devkit image
make sanity      # check dataset path + CUDA
make train_cp    # stub: creates outputs/cp_mini_debug/metrics.json
make eval_cp     # stub: updates metrics.json
make timing      # stub: logs latency numbers into metrics.json
make demo        # stub: writes a demo GIF (copied to docs/artifacts)
make bev         # render LIDAR_TOP BEV density (sanity figure)

## Quick artifacts
- BEV sanity image: `docs/artifacts/sanity_bev.png`
- Cluster baseline viz: `docs/artifacts/cluster_viz.png`
- Demo GIF (stub): `docs/artifacts/cp_demo.gif`
- nuScenes-style detections JSON (baseline): `docs/artifacts/nusc_results.json`

