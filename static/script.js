class TableManager
{
	constructor()
	{
		this.sortDirectionBtn = document.getElementById('sort-direction');
		this.sortDirectionBtn.addEventListener('change', (event) =>
		{
			this.fetchData(event.target.value);
		});

		this.fetchData('desc');
	}

	fillTable(bugDataArr)
	{
		let tableBody = document.querySelector('#table-body');
		tableBody.innerHTML = '';
		for(let i = 0; i < bugDataArr.length; i++)
		{
			let row = tableBody.insertRow(i);
			row.insertCell(0).innerHTML = String(i + 1);
			row.insertCell(1).innerHTML = bugDataArr[i].id;
			row.insertCell(2).innerHTML = (new Date (bugDataArr[i].date * 1000)).toLocaleDateString();

			let statusCell = row.insertCell(3)
			if(bugDataArr[i].status === 0)
			{
				statusCell.innerHTML = 'Neu';
				statusCell.classList.add("text-danger")
			}
			else if(bugDataArr[i].status === 1)
			{
				statusCell.innerHTML = 'In Bearbeitung';
				statusCell.classList.add("text-warning")
			}
			else
			{
				statusCell.innerHTML = 'Gelöst';
				statusCell.classList.add("text-success")
			}

			let priorityCell = row.insertCell(4)
			if(bugDataArr[i].priority === 0)
			{
				priorityCell.innerHTML = 'Mittel';
				priorityCell.classList.add("text-success")
			}
			else if(bugDataArr[i].priority === 1)
			{
				priorityCell.innerHTML = 'Hoch';
				priorityCell.classList.add("text-warning")
			}
			else
			{
				priorityCell.innerHTML = 'Sehr Hoch';
				priorityCell.classList.add("text-danger")
			}
			row.insertCell(5).innerHTML = bugDataArr[i].description;
			row.insertCell(6).innerHTML = bugDataArr[i].affected_users;
		}
	}

	async fetchData(sortDirection)
	{
		try
		{
			const response = await fetch(`http://localhost:5000/sort?dir=${sortDirection}`);
			const data = await response.json();
			this.fillTable(data.data);
		}
		catch(error)
		{
			console.error('Error:', error);
		}
	}
}

new TableManager();