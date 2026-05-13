import numpy as np

def dice_score(
    pred: np.ndarray,        # integer labels, shape (B, ...) — any spatial dims
    target: np.ndarray,      # integer labels, same shape as pred
    num_classes: int,
    ignore_index: int = -1,  # voxels with this label are excluded from computation
) -> tuple[np.ndarray, float]:
    """
    Compute per-class Dice score and the mean Dice across classes.

    Args:
        pred:        predicted class labels, shape (B, ...).
        target:      ground-truth class labels, same shape as pred.
        num_classes: total number of classes (labels are in [0, num_classes - 1]).
        ignore_index: a label value to be excluded from the computation
                      (e.g., -1 for "unlabeled" voxels).

    Returns:
        per_class_dice: np.ndarray of shape (num_classes,), Dice score per class.
                        If a class has no voxels in both pred AND target,
                        set its Dice to NaN (so it can be excluded from the mean).
        mean_dice:      float, mean Dice across classes that are NOT NaN.
    """
    if pred.shape != target.shape:
        raise ValueError(
            f"pred and target must have the same shape, "
            f"got {pred.shape} vs {target.shape}"
        )

    # Mask out voxels marked as ignore_index in the GT
    valid = (target != ignore_index)

    per_class_dice = np.full(num_classes, np.nan, dtype=np.float64)

    for c in range(num_classes):
        pred_mask = (pred == c) & valid
        target_mask = (target == c) & valid

        intersection = np.sum(pred_mask & target_mask)
        denom = np.sum(pred_mask) + np.sum(target_mask)

        if denom > 0:
            per_class_dice[c] = 2.0 * intersection / denom
        # else: leave as NaN (class absent in both pred and target)

    if np.all(np.isnan(per_class_dice)):
        mean_dice = float('nan')
    else:
        mean_dice = float(np.nanmean(per_class_dice))

    return per_class_dice, mean_dice