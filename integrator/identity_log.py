from rich.console import Console

console = Console()

def log_step(before, after, note):
    if before != after:
        console.print(f"[bold green]{note}[/bold green]")
        console.print(f"  Before: {before}")
        console.print(f"  After : {after}\n")