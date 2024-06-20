from invoke import Collection

from . import apps
from . import hybrid
from . import coco
from . import containerd
from . import cosign
from . import format_code
from . import gc
from . import k8s

ns = Collection(
    apps,
    coco,
    hybrid,
    containerd,
    cosign,
    format_code,
    gc,
    k8s,
    k9s,
    kata,
    kbs,
    knative,
    kubeadm,
    nydus_snapshotter,
    operator,
    ovmf,
    qemu,
    registry,
    sev,
    skopeo,
)

ns.add_collection(eval_ns, name="eval")
ns.add_collection(profile_ns, name="profile")
