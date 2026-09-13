export interface ArchitectureSignature {
  required_nodes: Set<string>;
  optional_nodes: Set<string>;
}

export class SignatureEngine {
  load_signatures(): Record<string, ArchitectureSignature> {
    return {
      MVC: {
        required_nodes: new Set(["controllers", "views", "models"]),
        optional_nodes: new Set(["templates", "routes"])
      },
      MVVM: {
        required_nodes: new Set(["views", "viewmodels"]),
        optional_nodes: new Set(["models"])
      },
      DDD: {
        required_nodes: new Set(["domain", "application", "infrastructure"]),
        optional_nodes: new Set(["entities", "repositories"])
      },
      "Event-Driven": {
        required_nodes: new Set(["events", "handlers"]),
        optional_nodes: new Set(["queues", "dispatchers"])
      },
      "Flow_Based_Architecture": {
        required_nodes: new Set(["components", "connections"]),
        optional_nodes: new Set(["subflows"])
      }
    };
  }
}
