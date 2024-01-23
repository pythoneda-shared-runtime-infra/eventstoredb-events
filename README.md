# Runtime EventStoreDB infrastructure events

This package declares the infrastructure events relevant to [https://www.eventstore.com](EventStoreDB "EventStoreDB").

## How to declare it in your flake

Check the latest tag of the artifact repository: https://github.com/pythoneda-shared-runtime-infra-def/eventstoredb-events/tags, and use it instead of the `[version]` placeholder below.

```nix
{
  description = "[..]";
  inputs = rec {
    [..]
    pythoneda-shared-runtime-infrastructure-eventstoredb-events = {
      [optional follows]
      url =
        "github:pythoneda-shared-runtime-infra-def/eventstoredb-events/[version]";
    };
  };
  outputs = [..]
};
```

Should you use another PythonEDA modules, you might want to pin those also used by this project. The same applies to [https://nixos/nixpkgs](nixpkgs "nixpkgs") and [https://github.com/numtide/flake-utils](flake-utils "flake-utils").

The Nix flake is managed by the [https://github.com/pythoneda-shared-runtime-infra-def/eventstoredb-events](eventstoredb-events "eventstored-events") definition repository.

